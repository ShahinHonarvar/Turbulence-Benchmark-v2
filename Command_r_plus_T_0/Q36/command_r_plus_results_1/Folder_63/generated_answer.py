def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 26 <= i < 80 and char > '<' and (char < '>'):
            continue
        result.append(char)
    return ''.join(result)