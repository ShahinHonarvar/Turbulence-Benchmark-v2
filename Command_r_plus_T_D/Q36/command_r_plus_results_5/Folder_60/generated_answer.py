def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 23 <= i < 83 and 'f' < char < 'o':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)