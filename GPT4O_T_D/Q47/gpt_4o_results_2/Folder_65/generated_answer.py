import re

def palindromes_of_specific_lengths(s):
    lower_s = s.lower()
    substring = lower_s[15:96]
    substring_letters_only = re.sub('[^a-zA-Z]', '', substring)
    palindromes = set()
    length = len(substring_letters_only)
    for l in range(20, 67):
        for i in range(length - l + 1):
            part = substring_letters_only[i:i + l]
            if part == part[::-1]:
                palindromes.add(part)
    return palindromes