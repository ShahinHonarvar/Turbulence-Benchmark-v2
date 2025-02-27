def filter_chars(s: str) -> str:
    result = []
    to_remove = set()
    for i, char in enumerate(s, start=421):
        if 68 < ord(char) < 74 and i < 854:
            to_remove.add(char)
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)