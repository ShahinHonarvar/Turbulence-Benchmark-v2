def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 'F' <= char <= 'h' and 19 <= i <= 90:
            continue
        result.append(char)
    return ''.join(result)