def filter_chars(s: str) -> str:
    result = []
    remove_chars = [chr(i) for i in range(ord('f') + 1, ord('{'))]
    for char in s:
        if 81 <= s.index(char) < 89 and char in remove_chars:
            continue
        result.append(char)
    return ''.join(result)