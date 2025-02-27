def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 51 < i < 76 and '5' < char < 'f':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)