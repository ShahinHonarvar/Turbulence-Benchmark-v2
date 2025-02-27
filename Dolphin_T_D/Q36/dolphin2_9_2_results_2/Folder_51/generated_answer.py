def filter_chars(s):
    for c in range(58, 81):
        if '5' < s[c] < '>' and s[c].isalpha():
            s = s.replace(s[c], '')
    return s