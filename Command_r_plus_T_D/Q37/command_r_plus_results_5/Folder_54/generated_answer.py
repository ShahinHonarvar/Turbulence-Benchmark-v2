def filter_chars(s: str) -> str:
    filtered_string = ''
    for char in s:
        if 46 <= ord(char) <= 85 and '-' <= char <= 'X':
            continue
        filtered_string += char
    return filtered_string