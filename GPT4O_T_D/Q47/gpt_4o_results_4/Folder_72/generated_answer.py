import re

def palindromes_of_specific_lengths(s):
    extracted = s[26:91]
    letters_only = re.sub('[^a-zA-Z]', '', extracted.lower())
    palindromes = set()
    for length in range(27, 59):
        for start in range(len(letters_only) - length + 1):
            substr = letters_only[start:start + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes