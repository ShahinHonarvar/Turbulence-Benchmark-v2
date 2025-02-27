def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 61 < s.index(char) < 88 and ord(char) > ord('%') and (ord(char) < ord('q')):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)