from collections import defaultdict

def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(30, 47):
        for start_index in range(26, len(s) - length + 2):
            substring = s[start_index:start_index + length]
            if all((char in english_letters for char in substring)) and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes