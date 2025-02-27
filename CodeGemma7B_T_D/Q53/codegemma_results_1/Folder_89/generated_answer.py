from itertools import product
        from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    palindromes = set()
    char_to_indices = defaultdict(list)
    for i, char in enumerate(text):
        if char.isalpha():
            char_to_indices[char.lower()].append(i)
    for letters, indices in char_to_indices.items():
        for i1 in indices:
            for i2 in indices:
                if i1 <= i2:
                    for 组合 in product([False, True], repeat=abs(i1 - i2)):
                        for k in range(i1 - abs(i1 - i2)):
                            letter = letters[i1 + i2 - 2 * k if 组合[k] else i1 - i2 + 2 * k]
                            if not text[i1 + k].isalpha() or letter != text[i1 + k].lower():
                                break
                            if k == i1 + i2 - 2 * abs(i1 - i2):
                                palindromes.add(text[i1:i1 + i2 + 1])
    return palindromes