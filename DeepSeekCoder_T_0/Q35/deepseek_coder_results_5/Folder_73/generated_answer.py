def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    start = 10
    end = min(76, len(s))
    repeat_chars = {c for c in s[start:end] if s[start:end].count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))