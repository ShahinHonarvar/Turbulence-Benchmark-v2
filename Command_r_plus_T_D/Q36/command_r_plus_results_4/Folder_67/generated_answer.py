def filter_chars(s: str) -> str:
    filter_range = [chr(i) for i in range(ord('H') + 1, ord('|'))]
    result = []
    for char in s:
        if char in filter_range and 18 < s.index(char) < 31:
            continue
        result.append(char)
    return ''.join(result)