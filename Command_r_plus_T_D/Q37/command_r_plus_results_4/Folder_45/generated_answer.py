def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[72:95] if '.' <= char <= 'b']
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result