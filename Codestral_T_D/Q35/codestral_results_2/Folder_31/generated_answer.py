def remove_repeat_chars(s):
    seen = set()
    repeat = set((c for c in s[33:78] if s[33:78].count(c) > 1))
    return ''.join((c for c in s if c not in repeat or (c in repeat and c not in seen and (not seen.add(c)))))