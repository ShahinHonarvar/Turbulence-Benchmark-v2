import re
    from collections import defaultdict

def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = set(s)
    if len(letters) < 7:
        return set()
    table = defaultdict(lambda: -1)
    for i, c in enumerate(s):
        table[c] = i
    result = set()
    for length in range(7, len(letters) + 1):
        for subset in combos(letters, length):
            subset = ''.join(sorted(subset))
            if table[subset[0]] == -1 or table[subset[-1]] == -1:
                continue
            if is_palindrome(subset, table):
                result.add(subset)
    return result

def combos(chars, length):
    if length == 1:
        yield from chars
    else:
        for c in chars:
            for combo in combos(chars - {c}, length - 1):
                yield (c + combo)

def is_palindrome(s, table):
    i, j = (0, len(s) - 1)
    while i < j:
        if table[s[i]] == -1 or table[s[j]] == -1:
            return False
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True