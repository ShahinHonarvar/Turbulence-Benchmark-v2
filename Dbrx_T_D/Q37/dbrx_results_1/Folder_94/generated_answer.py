def filter_chars(s):
    filtered_s = ''
    for i in range(len(s)):
        if s[i] >= 'X' and s[i] <= 'p' and (51 <= i < 96):
            continue
        filtered_s += s[i]
    return filtered_s