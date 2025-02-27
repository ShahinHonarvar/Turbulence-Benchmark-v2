def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[18:31] if 'H' < char < '|']
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result