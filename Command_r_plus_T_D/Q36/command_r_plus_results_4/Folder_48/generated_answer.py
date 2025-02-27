def filter_chars(s: str) -> str:
    filter_range = range(154, 223)
    filter_chars = [chr(i) for i in range(ord('A') + 1, ord('f'))]
    result = list(s)
    for i in filter_range:
        if s[i] in filter_chars:
            while s[i] in result:
                result.remove(s[i])
    return ''.join(result)