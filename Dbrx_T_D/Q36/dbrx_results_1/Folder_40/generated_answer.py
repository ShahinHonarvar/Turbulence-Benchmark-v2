def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, char in enumerate(s):
        if 1 < i < 7:
            if ord(char) > ord('-') and ord(char) < ord('L'):
                continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)