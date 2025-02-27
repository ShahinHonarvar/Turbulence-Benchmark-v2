def filter_chars(s):
    char_set = set(s[20:63])
    result = ''
    for ch in s:
        if ch < 'i' or ch > 'k' or ch not in char_set:
            result += ch
    return result