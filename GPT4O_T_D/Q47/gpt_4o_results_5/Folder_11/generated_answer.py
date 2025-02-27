import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[24:98]
    substring = re.sub('[^a-zA-Z]', '', substring)
    substring = substring.lower()
    length = len(substring)
    for start in range(length):
        for end in range(start + 10, min(start + 37, length + 1)):
            segment = substring[start:end]
            if segment == segment[::-1]:
                palindromes.add(segment)
    return palindromes