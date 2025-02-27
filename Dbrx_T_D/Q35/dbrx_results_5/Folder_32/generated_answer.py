def remove_repeat_chars(s: str) -> str:
    start, end = (85, 90)
    char_count = {}
    for i in range(len(s)):
        if s[i] in char_count and i > start and (i < end):
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
        if i >= start and i < end and (char_count[s[i]] > 1):
            s = s[:i] + s[i + 1:]
            i -= 1
    return s