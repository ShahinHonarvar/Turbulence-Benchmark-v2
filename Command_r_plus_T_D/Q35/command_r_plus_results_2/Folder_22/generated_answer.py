def remove_repeat_chars(s: str) -> str:
    seen = set()
    result = []
    for char in s:
        if 50 <= len(result) < 200:
            if char in seen:
                continue
            seen.add(char)
        result.append(char)
    return ''.join(result)