import re

def palindromes_of_specific_lengths(s):
    s = re.sub('[^a-zA-Z]', '', s[21:63]).lower()
    palindromes = set()
    for length in range(22, 34):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes