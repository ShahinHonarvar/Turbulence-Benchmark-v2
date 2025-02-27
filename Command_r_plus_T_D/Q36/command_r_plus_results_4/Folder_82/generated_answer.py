def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 69 <= i < 97 and 'V' < char < 'j':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)