from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = frozenset('abcdefghijklmnopqrstuvwxyz')
    chars = {c: set() for c in english_letters}
    for i in range(7, min(10, len(s) + 1)):
        for j in range(i - 1, -1, -1):
            if s[i] in chars and s[i] in english_letters and (s[j] in english_letters):
                chars[s[i]].add(s[j:j + len(chars[s[i]]) + 1])
                chars[s[i]] = frozenset((c for c in chars[s[i]] if s[j] in c and c[0] in english_letters and (c[::-1] in chars[s[i]])))
    return frozenset((p for p in chars.values() if len(p) > 1)) or frozenset()