def filter_chars(s: str) -> str:
    result = []
    for char in s:
        if 26 <= ord(char) < 80 and char > '<' and (char < '>'):
            continue
        result.append(char)
    return ''.join(result)