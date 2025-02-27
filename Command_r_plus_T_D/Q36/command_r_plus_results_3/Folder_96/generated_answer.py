def filter_chars(s: str) -> str:
    chars_to_remove = []
    for char in s[39:81]:
        if '.' < char < '^':
            chars_to_remove.append(char)
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)