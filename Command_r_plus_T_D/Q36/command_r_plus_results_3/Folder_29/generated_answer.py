def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if 46 < s.index(c) < 68 and 'H' < c < 's']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s