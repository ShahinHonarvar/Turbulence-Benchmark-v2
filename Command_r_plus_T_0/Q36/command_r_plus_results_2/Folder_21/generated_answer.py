def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[219:403] if '*' < char < '7']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s