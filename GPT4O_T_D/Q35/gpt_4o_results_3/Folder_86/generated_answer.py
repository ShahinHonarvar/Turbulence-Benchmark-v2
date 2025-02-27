def remove_repeat_chars(s):
    if len(s) <= 20:
        return s
    start = 20
    end = 32
    to_remove = set((c for c in s[start:end] if s[start:end].count(c) > 1))
    return ''.join((c for c in s if c not in to_remove or not start < s.index(c) < end))