def remove_repeat_chars(s: str) -> str:
    char_count = {}
    start, end = (49, 74)
    for i in range(len(s)):
        if i < start or i >= end:
            continue
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    unique_chars = []
    for i in range(len(s)):
        if i < start or i >= end:
            unique_chars.append(s[i])
            continue
        if char_count[s[i]] == 1:
            unique_chars.append(s[i])
    return ''.join(unique_chars)