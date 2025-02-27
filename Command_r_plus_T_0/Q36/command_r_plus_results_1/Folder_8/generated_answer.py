def filter_chars(s: str) -> str:
    chars_to_remove = set(s[82:93])
    chars_to_remove = {char for char in chars_to_remove if '!' < char < '*'}
    s_filtered = ''.join((char for char in s if char not in chars_to_remove))
    return s_filtered