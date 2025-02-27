def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 477 <= i <= 984 and ',' <= char <= 'V':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)