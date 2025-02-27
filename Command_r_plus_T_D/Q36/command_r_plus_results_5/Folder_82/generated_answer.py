def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 69 <= i < 97 and 'V' < char < 'j':
            continue
        result.append(char)
    return ''.join(result)