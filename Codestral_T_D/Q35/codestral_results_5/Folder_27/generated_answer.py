def remove_repeat_chars(s):
    section = s[86:89]
    seen = set()
    duplicates = set()
    for char in section:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return ''.join((char for char in s if char not in duplicates))