def filter_chars(s: str) -> str:
    for i in range(len(s)):
        if 71 <= i <= 96 and '_' <= s[i] <= 'o':
            while s[i] in s:
                s = s.replace(s[i], '')
    return s