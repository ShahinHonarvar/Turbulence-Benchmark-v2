def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('3') + 1, ord('B'))]
    result = []
    for char in s:
        if 18 < s.index(char) < 64 and char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)