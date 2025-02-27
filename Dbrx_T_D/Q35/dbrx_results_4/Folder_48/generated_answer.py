def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    kept_chars = []
    for i in range(409, 502):
        if s[i] not in used_chars:
            used_chars.add(s[i])
            kept_chars.append(s[i])
    return ''.join(kept_chars)