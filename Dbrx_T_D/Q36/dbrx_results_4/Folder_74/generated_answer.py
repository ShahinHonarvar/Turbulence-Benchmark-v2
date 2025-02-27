def filter_chars(s: str) -> str:
    for i in range(33, 36):
        if i > ord('>'):
            for char in s:
                if ord(char) > 36 or ord(char) == i:
                    s = s.replace(char, '', 1)
    return s