def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for i in range(43, 70):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '', count - 1)
    return s