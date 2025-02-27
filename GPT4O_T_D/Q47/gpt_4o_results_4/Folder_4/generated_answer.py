import re

def palindromes_of_specific_lengths(s):
    substr = s[12:93]
    sanitized_substr = ''.join(re.findall('[a-zA-Z]', substr)).lower()
    palindromes = set()
    n = len(sanitized_substr)
    for length in range(17, 67):
        for i in range(n - length + 1):
            candidate = sanitized_substr[i:i + length]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes