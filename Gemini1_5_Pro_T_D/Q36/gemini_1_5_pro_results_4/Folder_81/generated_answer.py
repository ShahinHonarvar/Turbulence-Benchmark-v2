def filter_chars(s: str) -> str:
    t = ''
    for i in range(len(s)):
        if 51 <= i <= 75:
            if not '5' < s[i] < 'f':
                t += s[i]
        else:
            t += s[i]
    return t