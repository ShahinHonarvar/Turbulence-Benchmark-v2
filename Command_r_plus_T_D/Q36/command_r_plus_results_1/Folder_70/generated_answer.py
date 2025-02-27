def filter_chars(s: str) -> str:
    chars_to_remove = []
    for i in range(170, 195):
        if ord(s[i]) > ord('!') and ord(s[i]) < ord('}'):
            chars_to_remove.append(s[i])
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)