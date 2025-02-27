def filter_chars(s: str) -> str:
    filtered_string = []
    for index, char in enumerate(s):
        if 'W' <= char <= '{' and 15 <= index <= 55:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)