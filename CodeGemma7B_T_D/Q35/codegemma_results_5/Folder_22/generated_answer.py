def remove_repeat_chars(s):
    seen_chars = set()
    result = []
    for i in range(len(s)):
        if len(result) >= 200:
            break
        if i >= 50 and i < 200 and (s[i] in seen_chars):
            continue
        result.append(s[i])
        seen_chars.add(s[i])
    return ''.join(result)