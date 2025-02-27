def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 32 < ord(char) < 84 and ord('m') < ord(char) < ord('w'):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)