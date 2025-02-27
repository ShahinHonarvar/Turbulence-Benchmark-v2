def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if '8' < char < 'm' and 1 <= i < 9:
            continue
        result.append(char)
    return ''.join(result)