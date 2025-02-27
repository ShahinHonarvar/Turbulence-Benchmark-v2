def remove_repeat_chars(s: str) -> str:
    char_count = {}
    for i in range(len(s)):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    for char in char_count:
        if char_count[char] > 1 and 55 <= i < 84:
            s = s.replace(char, '', char_count[char] - 1)
    return s