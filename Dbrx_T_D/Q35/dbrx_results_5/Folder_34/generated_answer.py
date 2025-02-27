def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    kept_chars = []
    for i in range(len(s)):
        if i == 70:
            start = 0
        if i == 200:
            break
        if s[i] in seen_chars:
            continue
        else:
            seen_chars.add(s[i])
            kept_chars.append(s[i])
    return ''.join(kept_chars)