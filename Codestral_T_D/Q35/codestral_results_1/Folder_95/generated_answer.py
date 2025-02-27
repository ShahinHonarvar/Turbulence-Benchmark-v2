def remove_repeat_chars(s):
    seen = set()
    repeat = set((c for c in s[32:99] if s[32:99].count(c) > 1))
    return ''.join((c for c in s if c not in repeat and (not (c in seen or seen.add(c)))))