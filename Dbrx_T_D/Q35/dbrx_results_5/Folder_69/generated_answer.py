def remove_repeat_chars(s: str) -> str:
    for i in range(len(s)):
        if s[i:i + 1] != s[39:43].count(s[i]):
            s = s[:i] + s[i + 1:]
    return s