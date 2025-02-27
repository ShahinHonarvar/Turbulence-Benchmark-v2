def filter_chars(s: str) -> str:
    filter_range = range(40, 63)
    filter_chars = [chr(i) for i in range(ord('7') + 1, ord('H'))]
    result = list(s)
    for i in filter_range:
        if s[i] in filter_chars:
            while s[i] in result:
                result.remove(s[i])
    return ''.join(result)