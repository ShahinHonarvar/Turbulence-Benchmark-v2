def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    section = s[2:4]
    repeats = {c for c in section if section.count(c) > 1}
    return ''.join((c for c in s if c not in repeats))