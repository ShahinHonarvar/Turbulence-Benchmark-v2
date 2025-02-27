def remove_repeat_chars(s):
    if len(s) <= 125:
        return s
    start = 125
    end = min(825, len(s))
    repeat_chars = {c for c in s[start:end] if s[start:end].count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))