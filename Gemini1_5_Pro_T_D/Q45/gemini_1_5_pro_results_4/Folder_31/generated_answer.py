from collections import Counter

def palindromes_between_indices(string):
    string = string[1:9].lower()
    letters = ''.join((ch for ch in string if ch.isalpha()))
    letters_counts = Counter(letters)
    palindrome_set = set()
    for i in range(3, len(letters) + 1):
        for key, value in letters_counts.items():
            if value >= 2 and i // 2 >= 1:
                if i % 2 == 0:
                    palindrome = key * (i // 2) + i // 2 * key[::-1]
                else:
                    for key2, value2 in letters_counts.items():
                        if key2 != key and value2 >= 1:
                            palindrome = key * (i // 2) + key2 + i // 2 * key[::-1]
                            if len(palindrome) >= 6:
                                palindrome_set.add(palindrome)
    return palindrome_set