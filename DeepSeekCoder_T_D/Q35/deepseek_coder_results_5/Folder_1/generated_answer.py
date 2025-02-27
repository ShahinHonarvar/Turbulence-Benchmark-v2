def remove_repeat_chars(s):
    if len(s) <= 17:
        return s
    start = 17
    end = min(88, len(s))
    repeat_chars = {c for c in s[start:end] if s[start:end].count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))