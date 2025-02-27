def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 49 < ord(char) < 56:
            if char > 'I' and char < 'a':
                continue
        filtered_string.append(char)
    return ''.join(filtered_string)