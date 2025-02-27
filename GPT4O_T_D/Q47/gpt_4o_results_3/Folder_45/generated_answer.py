import re

def palindromes_of_specific_lengths(s):
    s = s[70:141]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    n = len(s)
    palindromes = set()
    for length in range(3, 61):
        for i in range(n - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes