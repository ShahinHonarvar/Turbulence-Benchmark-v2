def filter_chars(s: str) -> str:
    chars_to_remove = [chr for chr in s[588:648] if chr > ',' and chr < 'c']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s