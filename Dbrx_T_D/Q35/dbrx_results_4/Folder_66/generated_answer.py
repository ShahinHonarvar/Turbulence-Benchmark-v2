def remove_repeat_chars(s: str) -> str:
    seen = set()
    result = []
    start, end = (11, 76)
    for i in range(start, end):
        if s[i] in seen:
            continue
        seen.add(s[i])
        result.append(s[i])
    return ''.join(result) + s[end:]