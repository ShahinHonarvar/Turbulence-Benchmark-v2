def filter_chars(s):
    s_list = list(s)
    for i in range(75, 100):
        if i < len(s) and '8' <= s[i] <= 'e':
            s_list = [c for c in s_list if c != s[i]]
    return ''.join(s_list)