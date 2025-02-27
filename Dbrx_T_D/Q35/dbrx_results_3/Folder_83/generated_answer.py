def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    kept_chars = []
    for i, char in enumerate(s):
        if i >= 100 and i < 200:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
                kept_chars.append(char)
        elif i < 100 or i >= 200:
            kept_chars.append(char)
    return ''.join(kept_chars)