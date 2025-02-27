def remove_repeat_chars(s):
    start, end = (43, 70)
    if start < len(s):
        sub_s = s[start:end]
        repeat_chars = {c for c in sub_s if sub_s.count(c) > 1}
        result = s[:start] + ''.join((c for c in s[start:end] if c not in repeat_chars)) + s[end:]
        return result
    return s