def filter_chars(s: str) -> str:
    filter_range = [char for char in s[72:95] if char >= '.' and char <= 'b']
    for char in filter_range:
        s = s.replace(char, '')
    return s