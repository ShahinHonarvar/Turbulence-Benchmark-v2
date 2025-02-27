def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 323 < i < 526 and char > ')' and (char < 'O'):
            continue
        result.append(char)
    return ''.join(result)