def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    result = []
    for char in s[90:97]:
        if char not in seen_chars:
            seen_chars.add(char)
            result.append(char)
    return ''.join(result) + s[:90] + s[97:]