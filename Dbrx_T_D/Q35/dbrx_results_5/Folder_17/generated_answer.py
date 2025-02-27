def remove_repeat_chars(s: str) -> str:
    for char in set(s[73:84]):
        if s[73:84].count(char) > 1:
            s = s[:73] + s[73:84].replace(char, '', s[73:84].count(char) - 1) + s[84:]
    return s