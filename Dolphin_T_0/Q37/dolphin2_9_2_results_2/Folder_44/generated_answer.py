def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 21 <= i <= 43 and s[i] >= '+' and (s[i] <= '8'):
            continue
        else:
            result += s[i]
    return result