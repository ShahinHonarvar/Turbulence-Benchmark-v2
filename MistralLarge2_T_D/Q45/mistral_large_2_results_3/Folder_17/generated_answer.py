import re

def palindromes_between_indices(s):
    chars = re.findall('[a-zA-Z]', s[2:7])
    chars = ''.join(chars).lower()
    palindromes = set()
    for length in range(4, len(chars) + 1):
        for start in range(len(chars) - length + 1):
            substr = chars[start:start + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes