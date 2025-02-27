def filter_chars(s: str) -> str:
    filtered_string = []
    for index, char in enumerate(s):
        if not (36 <= index <= 79 and 'a' <= char <= 'i'):
            filtered_string.append(char)
    return ''.join(filtered_string)