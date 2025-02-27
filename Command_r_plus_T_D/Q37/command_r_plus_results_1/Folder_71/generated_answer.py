def filter_chars(s: str) -> str:
    filtered_string = ''
    for char in s:
        if 32 <= ord(char) <= 46 and '0' <= char <= 'k':
            continue
        filtered_string += char
    return filtered_string