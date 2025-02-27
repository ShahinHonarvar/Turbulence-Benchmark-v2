def filter_chars(s: str) -> str:
    result = []
    to_remove = set()
    for i, char in enumerate(s):
        if 476 < i < 948 and 'b' < char < 'd':
            to_remove.add(char)
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)