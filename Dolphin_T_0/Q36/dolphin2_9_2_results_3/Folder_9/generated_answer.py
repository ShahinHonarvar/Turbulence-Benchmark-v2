def filter_chars(s):
    s_lst = list(s)
    for i in range(50, 92):
        if 'A' < s_lst[i] < 'Q':
            s_lst = [c for c in s_lst if c != s_lst[i]]
    return ''.join(s_lst)