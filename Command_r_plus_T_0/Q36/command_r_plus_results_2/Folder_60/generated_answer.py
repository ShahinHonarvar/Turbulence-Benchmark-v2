def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 'f' < char < 'o' and 23 <= i < 83:
            continue
        result.append(char)
    return ''.join(result)