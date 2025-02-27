def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for i in range(len(s)):
        if s[i] not in char_count:
            char_count[s[i]] = 1
        else:
            char_count[s[i]] += 1
    for i in range(27, 97):
        if chr(i) in char_count and char_count[chr(i)] > 1:
            s = s.replace(chr(i), '', char_count[chr(i)] - 1)
    return s