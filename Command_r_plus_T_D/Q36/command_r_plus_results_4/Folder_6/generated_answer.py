def filter_chars(s: str) -> str:
    new_s = ''
    for char in s:
        if 31 < ord(char) < 70 and ord(char) > ord('B') and (ord(char) < ord('v')):
            continue
        new_s += char
    return new_s