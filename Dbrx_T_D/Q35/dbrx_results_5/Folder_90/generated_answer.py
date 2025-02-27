def remove_repeat_chars(s):
    seen_chars = set()
    kept_chars = []
    for i in range(len(s)):
        if i < 306 or i > 807:
            kept_chars.append(s[i])
        elif s[i] not in seen_chars:
            seen_chars.add(s[i])
            kept_chars.append(s[i])
    return ''.join(kept_chars)