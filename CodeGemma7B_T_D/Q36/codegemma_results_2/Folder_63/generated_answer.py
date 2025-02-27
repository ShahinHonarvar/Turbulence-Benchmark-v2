def filter_chars(s):
    new_str = ''
    for i in range(len(s)):
        if i < 26 or i >= 80 or s[i] <= '<' or (s[i] >= '>'):
            new_str += s[i]
    return new_str