def filter_chars(s):
    if len(s) <= 477:
        return s
    section_part = s[477:948]
    chars_to_remove = {c for c in section_part if 'b' < c < 'd'}
    return ''.join((c for c in s if c not in chars_to_remove))