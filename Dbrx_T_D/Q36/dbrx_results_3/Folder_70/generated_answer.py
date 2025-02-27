def filter_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(170, 195):
        char = s[i]
        if '!' < char < '}':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        s = s.replace(char, '', 1)
    return s