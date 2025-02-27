def filter_chars(s: str) -> str:
    new_s = []
    for char in s:
        if 32 < ord(char) < 61 and '3' < char < 'D':
            continue
        new_s.append(char)
    return ''.join(new_s)