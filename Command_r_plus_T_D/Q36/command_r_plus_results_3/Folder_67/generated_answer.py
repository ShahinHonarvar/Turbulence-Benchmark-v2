def filter_chars(s: str) -> str:
    unwanted_chars = [char for char in s[18:31] if 'H' < char < '|']
    for char in unwanted_chars:
        s = s.replace(char, '')
    return s