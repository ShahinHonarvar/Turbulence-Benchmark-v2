def filter_chars(s: str) -> str:
    chars_to_remove = []
    for i in range(219, 403):
        if ord(s[i]) > ord('*') and ord(s[i]) < ord('7'):
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s