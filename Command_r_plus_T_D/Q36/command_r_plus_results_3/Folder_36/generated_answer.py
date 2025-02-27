def filter_chars(s: str) -> str:
    result = []
    remove_chars = [chr(i) for i in range(ord('l') + 1, ord('t'))]
    for char in s:
        if 283 < s.index(char) < 484 and char in remove_chars:
            continue
        result.append(char)
    return ''.join(result)