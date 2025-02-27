def remove_repeat_chars(s: str) -> str:
    char_counts = {}
    start, end = (42, 87)
    for i in range(start, end):
        if s[i] in char_counts:
            char_counts[s[i]] += 1
        else:
            char_counts[s[i]] = 1
    result = []
    for c in s[:start] + s[end:]:
        if c not in char_counts or char_counts[c] == 0:
            result.append(c)
    for i in range(start, end):
        if s[i] not in char_counts or char_counts[s[i]] == 0:
            result.append(s[i])
            if s[i] in char_counts:
                char_counts[s[i]] -= 1
    return ''.join(result)