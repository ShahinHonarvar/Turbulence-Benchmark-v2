import re

def palindromes_of_specific_lengths(s):
    substring = s[31:75]
    letters_only = re.sub('[^a-zA-Z]', '', substring).lower()
    palindromes = set()
    for length in range(23, 40):
        for start in range(len(letters_only) - length + 1):
            candidate = letters_only[start:start + length]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes