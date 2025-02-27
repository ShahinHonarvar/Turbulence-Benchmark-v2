def filter_chars(s: str) -> str:
    new_str = []
    for char in s:
        if 46 < ord(char) < 91 and ord('D') < ord(char) < ord('H'):
            continue
        new_str.append(char)
    return ''.join(new_str)