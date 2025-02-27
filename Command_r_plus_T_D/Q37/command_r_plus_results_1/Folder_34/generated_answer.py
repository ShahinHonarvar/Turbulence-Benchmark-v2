def filter_chars(s: str) -> str:
    filter_range = [char for char in s[54:63] if ')' <= char <= '9']
    for char in filter_range:
        s = s.replace(char, '')
    return s