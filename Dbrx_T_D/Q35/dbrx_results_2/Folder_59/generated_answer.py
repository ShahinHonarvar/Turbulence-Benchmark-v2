def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    result = []
    for char in s[1:11]:
        if char in seen_chars:
            continue
        seen_chars.add(char)
        result.append(char)
    return ''.join(result) + s[11:]