from collections import defaultdict

def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    if len(s) < 76:
        return set()
    table = defaultdict(bool, {s[i:j]: True for i in range(len(s)) for j in range(76 + i, len(s) + 1)})
    for i in range(len(s) - 76, -1, -1):
        for j in range(76 + i, len(s) + 1):
            if s[i:j] == s[i:j][::-1] and table[s[i:j]]:
                table[s[i:j]] = True
    return {p for p in table if table[p]}