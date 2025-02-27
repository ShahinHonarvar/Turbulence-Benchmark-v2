def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 63 and i <= 84 and (s[i] >= 'E') and (s[i] <= '~'):
            continue
        result += s[i]
    return result