def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[23:83] if 'f' < char < 'o']
    result = s
    for char in chars_to_remove:
        result = result.replace(char, '')
    return result