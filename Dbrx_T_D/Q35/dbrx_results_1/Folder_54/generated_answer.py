def remove_repeat_chars(s: str) -> str:
    occur_idx = set(s[34:64])
    chars = []
    for idx in range(len(s)):
        if idx < 34 or idx > 63 or s[idx] not in occur_idx:
            chars.append(s[idx])
    return ''.join(chars)