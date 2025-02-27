def remove_repeat_chars(s):
    if len(s) < 78:
        return s
    section = s[78:84]
    repeat_chars = {c for c in section if section.count(c) > 1}
    result = [c for c in s if c not in repeat_chars]
    return ''.join(result)