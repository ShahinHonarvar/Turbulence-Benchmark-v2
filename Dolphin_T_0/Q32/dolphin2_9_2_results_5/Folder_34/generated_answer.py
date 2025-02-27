def insert_after_character(s):
    out_str = ''
    for i in range(len(s)):
        if s[i] == 'A':
            out_str = out_str + s[i] + 'a'
        else:
            out_str = out_str + s[i]
    return out_str