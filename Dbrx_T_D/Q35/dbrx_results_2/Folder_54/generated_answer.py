def remove_repeat_chars(s: str) -> str:
    chars = set()
    for i in range(len(s)):
        if i >= 35 and i < 64 and (s[i] in chars):
            s = s[:i] + s[i + 1:]
            i -= 1
        else:
            chars.add(s[i])
    return s