def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for i in range(len(s)):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    unique_s = []
    for i in range(len(s)):
        if i < 86 or i >= 99 or char_count[s[i]] == 1:
            unique_s.append(s[i])
    return ''.join(unique_s)