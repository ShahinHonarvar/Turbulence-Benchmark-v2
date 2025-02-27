def filter_chars(s):
    t = ''
    for i in range(len(s)):
        if 82 <= i <= 93 and '!' < s[i] < '*':
            continue
        if 82 > i or i > 93:
            t += s[i]
        elif s[i] not in s[83:93]:
            t += s[i]
    return t