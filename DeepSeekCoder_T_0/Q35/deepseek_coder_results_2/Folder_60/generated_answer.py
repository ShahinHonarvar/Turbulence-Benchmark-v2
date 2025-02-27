def remove_repeat_chars(s):
    start, end = (38, 52)
    if start < len(s):
        sub_str = s[start:end]
        repeat_chars = {c for c in sub_str if sub_str.count(c) > 1}
        result = s[:start] + ''.join((c for c in s[start:end] if c not in repeat_chars)) + s[end:]
    else:
        result = s
    return result