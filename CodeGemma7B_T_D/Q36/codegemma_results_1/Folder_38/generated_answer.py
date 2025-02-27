def filter_chars(s):
    filtered_chars = ''
    for i in range(len(s)):
        if not (44 < i < 48 and s[i] > '+' and (s[i] < 'l')):
            filtered_chars += s[i]
    return filtered_chars