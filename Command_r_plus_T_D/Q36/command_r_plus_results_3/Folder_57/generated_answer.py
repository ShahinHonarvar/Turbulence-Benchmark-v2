def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 'A' < char < 'U' and 70 <= i < 74:
            continue
        result.append(char)
    return ''.join(result)