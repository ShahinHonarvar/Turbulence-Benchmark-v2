def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s[18:31] if 'H' < char < '|']
    return s.replace(''.join(filter(lambda char: char not in filtered_chars, s[18:31])), '', 1)