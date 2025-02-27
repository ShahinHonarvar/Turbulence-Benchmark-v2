def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 'A' <= char <= 'Q' and 38 <= i <= 99:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)