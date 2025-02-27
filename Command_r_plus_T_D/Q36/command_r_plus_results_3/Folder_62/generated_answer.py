def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 63 < i < 89 and ord(char) > ord('*') and (ord(char) < ord('w')):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)