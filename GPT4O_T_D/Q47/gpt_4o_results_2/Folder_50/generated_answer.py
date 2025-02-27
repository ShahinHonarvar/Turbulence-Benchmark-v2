import re

def palindromes_of_specific_lengths(s):
    substring = s[36:93]
    clean_substring = re.sub('[^A-Za-z]', '', substring).lower()
    palindromes = set()
    for start in range(len(clean_substring)):
        for end in range(start + 10, min(start + 36, len(clean_substring) + 1)):
            if clean_substring[start:end] == clean_substring[start:end][::-1]:
                palindromes.add(clean_substring[start:end])
    return palindromes