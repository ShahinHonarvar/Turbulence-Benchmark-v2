def remove_repeat_chars(s):
    chars = set()
    kept = []
    for i in range(13, 70):
        if s[i] not in chars:
            chars.add(s[i])
            kept.append(s[i])
    for j in range(min(70, len(s)), len(s)):
        kept.append(s[j])
    for k in range(13):
        kept.insert(k, s[k])
    return ''.join(kept)