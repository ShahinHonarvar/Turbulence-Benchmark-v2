def remove_repeat_chars(s: str) -> str:
    start, end = (34, 69)
    seen_chars = set()
    result = []
    for i, char in enumerate(s):
        if start <= i < end:
            if char in seen_chars:
                continue
            seen_chars.add(char)
        result.append(char)
    return ''.join(result)