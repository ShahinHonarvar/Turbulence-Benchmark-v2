def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 'I' < char < 'M' and 15 <= i < 85:
            continue
        result.append(char)
    return ''.join(result)