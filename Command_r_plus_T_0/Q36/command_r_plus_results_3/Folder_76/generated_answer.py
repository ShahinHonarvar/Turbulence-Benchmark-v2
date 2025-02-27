def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 669 < i < 888 and 'B' < char < 'Y':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)