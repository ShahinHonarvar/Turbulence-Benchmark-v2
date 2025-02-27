def filter_chars(s: str) -> str:
    chars_to_remove = set()
    for char in s[18:64]:
        if '3' < char < 'B':
            chars_to_remove.add(char)
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)