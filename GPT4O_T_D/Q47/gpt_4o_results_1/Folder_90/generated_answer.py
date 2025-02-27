import re

def palindromes_of_specific_lengths(s):
    substring = s[106:281]
    substring = re.sub('[^a-zA-Z]', '', substring).lower()
    n = len(substring)
    palindromes = set()
    for length in range(136, 152):
        for start in range(n - length + 1):
            sub = substring[start:start + length]
            if sub == sub[::-1]:
                palindromes.add(s[start + 106:start + 106 + length])
    return palindromes