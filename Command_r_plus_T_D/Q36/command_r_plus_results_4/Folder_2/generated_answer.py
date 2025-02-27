def filter_chars(s: str) -> str:
    result = []
    remove_chars = set()
    for i, char in enumerate(s[421:854], 421):
        if 'D' < char < 'J':
            remove_chars.add(char)
    for char in s:
        if char not in remove_chars:
            result.append(char)
    return ''.join(result)