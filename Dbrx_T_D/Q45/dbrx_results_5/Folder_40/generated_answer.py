import re

def palindromes_between_indices(s):
    s = s[4:10].lower()
    chars = set(s)
    palindromes = set()
    for c in chars:
        for i in range(7, len(s) + 1):
            substr = ''.join((j for j in s if j == c or j == '_'))
            if len(substr) < i:
                continue
            if re.match(f'({substr[0]}._)*{substr[0]}', substr[:i]) and substr[:i] == substr[i - 1::-1][:i]:
                palindromes.add(substr[:i])
    return palindromes