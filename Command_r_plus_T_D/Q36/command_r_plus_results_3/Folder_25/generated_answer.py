def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 'A' < char < 'h' and 24 <= i < 37:
            continue
        result.append(char)
    return ''.join(result)