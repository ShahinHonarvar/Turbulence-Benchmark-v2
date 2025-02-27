def filter_chars(s):
    new_s = ''
    for i in range(len(s)):
        if i >= 420 and i <= 853 and (s[i] > 'D') and (s[i] < 'J'):
            continue
        new_s += s[i]
    return new_s