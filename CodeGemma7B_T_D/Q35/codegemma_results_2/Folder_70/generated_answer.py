def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(len(s)):
        if i < 43 or i >= 70 or s[i] in seen:
            continue
        seen.add(s[i])
        result.append(s[i])
    return ''.join(result)