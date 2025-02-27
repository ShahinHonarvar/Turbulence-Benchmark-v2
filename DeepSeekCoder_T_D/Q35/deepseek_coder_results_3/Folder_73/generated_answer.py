def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    start = 10
    end = min(76, len(s))
    repeat_chars = {c for c in s[start:end] if s[start:end].count(c) > 1}
    result = s[:start] + ''.join((c for c in s[start:end] if c not in repeat_chars)) + s[end:]
    return result