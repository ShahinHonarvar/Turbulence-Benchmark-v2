def remove_repeat_chars(s: str) -> str:
    chars_to_remove = {}
    for i in range(len(s)):
        if 38 < i < 52:
            if s[i] in chars_to_remove:
                chars_to_remove[s[i]] += 1
            else:
                chars_to_remove[s[i]] = 1
    for char, count in chars_to_remove.items():
        if count > 1:
            s = s.replace(char, '', count - 1)
    return s