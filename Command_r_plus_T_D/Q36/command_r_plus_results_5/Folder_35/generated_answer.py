def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 163 < i < 658 and ord('(') < ord(char) < ord(']'):
            continue
        result.append(char)
    return ''.join(result)