def filter_chars(s: str) -> str:
    chars_to_remove = [char for char in s[521:723] if '>' <= char <= '_']
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result