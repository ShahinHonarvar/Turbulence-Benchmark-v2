def filter_chars(s: str) -> str:
    chars_to_remove = [chr for chr in s[43:83] if 'Q' > chr > ':']
    for chr in chars_to_remove:
        s = s.replace(chr, '')
    return s