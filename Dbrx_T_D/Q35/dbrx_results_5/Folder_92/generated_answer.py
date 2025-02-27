def remove_repeat_chars(s: str) -> str:
    chars_seen = set()
    result = []
    for char in s[1:-1]:
        if char in chars_seen:
            continue
        chars_seen.add(char)
        result.append(char)
    return ''.join(result) + s[0] + s[-1]