def remove_repeat_chars(s: str) -> str:
    for i in range(len(s)):
        if s[i:i + 1] in s[45:48] and s.count(s[i]) > 1:
            s = s.replace(s[i], '', 1)
    return s