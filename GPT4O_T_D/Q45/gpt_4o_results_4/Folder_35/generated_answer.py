from itertools import permutations

def palindromes_between_indices(s):
    idx_start, idx_end = (2, 5)
    sub_str = ''.join([char.lower() for char in s[idx_start:idx_end] if char.isalpha()])
    palindromes = set()
    for length in range(4, len(sub_str) + 1):
        for perm in permutations(sub_str, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes