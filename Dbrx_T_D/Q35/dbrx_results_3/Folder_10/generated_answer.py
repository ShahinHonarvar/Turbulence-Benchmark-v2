def remove_repeat_chars(s: str) -> str:
    for char in set(s[36:54]):
        if s[36:54].count(char) > 1:
            i = 36
            while i < len(s):
                if s[i] == char:
                    s = s[:i] + s[i + 1:]
                    i -= 1
                i += 1
    return s