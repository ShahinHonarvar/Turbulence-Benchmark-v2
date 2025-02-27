def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if not (722 <= i <= 832 and 'K' <= char <= 'm'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)