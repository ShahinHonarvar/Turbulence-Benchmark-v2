def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 'H' <= char <= 'e' and 38 <= i <= 69:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)