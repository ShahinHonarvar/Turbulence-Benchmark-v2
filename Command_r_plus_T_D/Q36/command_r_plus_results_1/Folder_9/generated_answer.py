def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 50 < i < 92 and 'A' < char < 'Q':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)