def filter_chars(s: str) -> str:
    start_index, end_index = (31, 73)
    chars_to_filter = [c for c in s[start_index:end_index] if 'M' < c < 'j']
    for char in chars_to_filter:
        s = s.replace(char, '', s.count(char))
    return s