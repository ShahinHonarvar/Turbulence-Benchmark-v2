def filter_chars(s: str) -> str:
    filtered_string = []
    for index, char in enumerate(s):
        if 'a' <= char <= 'i' and 36 <= index <= 79:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)