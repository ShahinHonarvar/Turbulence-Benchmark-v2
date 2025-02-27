def filter_chars(s: str) -> str:
    chars_to_remove = [chr for chr in s[43:83] if chr > ':' and chr < 'Q']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s