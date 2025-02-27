def remove_repeat_chars(s: str) -> str:
    char_set = set()
    start, end = (57, 85)
    for i in range(len(s)):
        if s[i] in char_set and start <= i < end:
            s = s[:i] + s[i + 1:]
            i -= 1
        elif i == end:
            char_set.clear()
        else:
            char_set.add(s[i])
    return s