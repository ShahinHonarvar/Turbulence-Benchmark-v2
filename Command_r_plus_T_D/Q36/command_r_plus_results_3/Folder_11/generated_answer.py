def filter_chars(s: str) -> str:
    filter_range = [char for char in s if 69 < ord(char) < 126 and 86 < s.index(char) < 94]
    for char in filter_range:
        s = s.replace(char, '')
    return s