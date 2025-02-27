def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    unique_chars = []
    for i in range(36, 85):
        if s[i] in seen_chars:
            continue
        if i < 36 or i >= 85:
            unique_chars.append(s[i])
        elif s[i] not in s[:i]:
            unique_chars.append(s[i])
        seen_chars.add(s[i])
    return ''.join(unique_chars)