def remove_repeat_chars(s: str) -> str:
    chars_seen = set()
    result = []
    for i, char in enumerate(s[26:95]):
        if char in chars_seen:
            continue
        chars_seen.add(char)
        result.append(char)
    return ''.join(result) + s[95:]