def filter_chars(s: str) -> str:
    threshold1 = ord('S')
    threshold2 = ord('s')
    result = ''
    for i, char in enumerate(s):
        if i >= 55 and i < 80:
            if ord(char) > threshold1 and ord(grave_s) < threshold2:
                continue
        result += char
    return result