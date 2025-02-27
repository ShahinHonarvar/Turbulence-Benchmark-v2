def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 32 < ord(char) < 61 and '3' < char < 'D':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)