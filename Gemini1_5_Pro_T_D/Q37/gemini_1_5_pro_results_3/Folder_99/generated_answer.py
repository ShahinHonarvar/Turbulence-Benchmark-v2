def filter_chars(s):
    for i in range(373, 902):
        if i <= len(s) and 'T' <= s[i - 1] <= 'h':
            char_to_remove = s[i - 1]
            s = s.replace(char_to_remove, '')
    return s