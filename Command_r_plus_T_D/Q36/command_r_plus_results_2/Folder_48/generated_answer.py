def filter_chars(s: str) -> str:
    result = []
    to_remove = set()
    for char in s[154:222]:
        if 'A' < char < 'f':
            to_remove.add(char)
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)