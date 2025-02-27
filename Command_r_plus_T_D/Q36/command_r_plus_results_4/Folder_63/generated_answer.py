def filter_chars(s: str) -> str:
    result = []
    for i, char in enumerate(s):
        if 26 <= i < 80 and ord(char) > ord('<') and (ord(char) < ord('>')):
            continue
        result.append(char)
    return ''.join(result)