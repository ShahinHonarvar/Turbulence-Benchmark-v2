def filter_chars(s):
    s_list = list(s)
    for i in range(34, 36):
        if '>' < s_list[i] < 'A':
            s_list = [char for char in s_list if char != s_list[i]]
    return ''.join(s_list)