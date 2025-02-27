def filter_chars(text):
    result = []
    seen = set()
    for i, char in enumerate(text):
        if 12 <= i <= 25 and 'P' <= char <= 'x':
            seen.add(char)
        elif char not in seen:
            result.append(char)
    return ''.join(result)