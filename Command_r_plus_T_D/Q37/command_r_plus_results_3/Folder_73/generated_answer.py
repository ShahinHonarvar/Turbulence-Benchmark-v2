def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 22 <= ord(char) <= 85 and '7' <= char <= 'e':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)