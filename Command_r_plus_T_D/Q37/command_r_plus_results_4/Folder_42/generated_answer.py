def filter_chars(s: str) -> str:
    filter_range = [chr for chr in s[73:75] if 'U' <= chr <= 'l']
    return ''.join((chr for chr in s if chr not in filter_range))