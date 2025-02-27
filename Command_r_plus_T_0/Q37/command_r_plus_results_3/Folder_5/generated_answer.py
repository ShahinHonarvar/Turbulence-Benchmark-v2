def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 24 <= i <= 82 and '5' <= char <= '<':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)