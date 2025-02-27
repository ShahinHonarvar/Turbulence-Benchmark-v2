def filter_chars(s: str) -> str:
    chars_to_remove = [chr for chr in s[13:29] if 'c' <= chr <= 'n']
    return ''.join((chr for chr in s if chr not in chars_to_remove))