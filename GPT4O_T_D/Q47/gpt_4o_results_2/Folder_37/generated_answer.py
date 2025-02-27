import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    target_substring = s[0:10]
    target_substring = re.sub('[^a-z]', '', target_substring)
    palindromes = set()
    for length in range(3, 6):
        for i in range(len(target_substring) - length + 1):
            substring = target_substring[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes