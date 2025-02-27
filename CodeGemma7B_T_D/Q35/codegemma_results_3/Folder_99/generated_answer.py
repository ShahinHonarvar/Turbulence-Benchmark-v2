def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(len(s)):
        if i >= 450 and i <= 905 and (s[i] in seen):
            continue
        seen.add(s[i])
        result.append(s[i])
    return ''.join(result)