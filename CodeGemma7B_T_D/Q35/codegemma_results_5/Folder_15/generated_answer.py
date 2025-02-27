def remove_repeat_chars(s):
    result = s[:5]
    seen = set(s[:5])
    for i in range(5, len(s)):
        if s[i] not in seen:
            result += s[i]
            seen.add(s[i])
    return result