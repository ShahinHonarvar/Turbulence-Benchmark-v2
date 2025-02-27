def remove_repeat_chars(s):
    seen = set()
    start, end = (450, 905)
    for i in range(len(s)):
        if s[i] in seen and start < i < end:
            s = s[:i] + s[i + 1:]
        elif s[i] not in seen:
            seen.add(s[i])
    return s