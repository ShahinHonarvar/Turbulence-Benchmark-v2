def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 38 <= i <= 69 and 'H' <= char <= 'e':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)