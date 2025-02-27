def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if ')' < char < 'P' and 18 <= i < 38:
            continue
        result.append(char)
    return ''.join(result)