def filter_chars(s: str) -> str:
    result = []
    for idx, char in enumerate(s):
        if 'W' <= char <= '{' and 15 <= idx <= 55:
            continue
        result.append(char)
    return ''.join(result)