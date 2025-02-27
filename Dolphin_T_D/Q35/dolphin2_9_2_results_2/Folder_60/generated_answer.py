def remove_repeat_chars(s):
    between_38_52 = s[38:52]
    duplicates = [c for c in between_38_52 if s.count(c) > 1]
    for duplicate in duplicates:
        s = s.replace(duplicate, '')
    return s