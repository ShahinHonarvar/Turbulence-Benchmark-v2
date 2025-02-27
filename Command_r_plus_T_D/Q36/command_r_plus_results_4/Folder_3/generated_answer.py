def filter_chars(s: str) -> str:
    filtered_chars = []
    for char in s[42:78]:
        if '!' < char < '?':
            filtered_chars.append(char)
    for char in filtered_chars:
        s = s.replace(char, '')
    return s