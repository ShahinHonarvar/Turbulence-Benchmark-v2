def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 10 <= i < 79 and '?' < char < 'm':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)