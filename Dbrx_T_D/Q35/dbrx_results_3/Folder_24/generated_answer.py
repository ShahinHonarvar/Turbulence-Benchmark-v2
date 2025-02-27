def remove_repeat_chars(s: str) -> str:
    chars_seen = set()
    start, end = (13, 91)
    result = []
    for i, c in enumerate(s):
        if start <= i < end:
            if c in chars_seen:
                continue
            chars_seen.add(c)
        result.append(c)
    return ''.join(result)