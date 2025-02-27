def remove_repeat_chars(s: str) -> str:
    chars_seen = set()
    result = []
    for i, c in enumerate(s):
        if i > 60 and i < 200 and (c in chars_seen):
            continue
        if c not in chars_seen:
            result.append(c)
            chars_seen.add(c)
    return ''.join(result)