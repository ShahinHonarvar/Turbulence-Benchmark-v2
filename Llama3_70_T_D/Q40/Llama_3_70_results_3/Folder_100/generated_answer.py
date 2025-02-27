def return_n_smallest_chars(s):
    s_list = []
    for char in s:
        s_list.append(char)
    s_list.sort()
    n_smallest_chars = s_list[:72]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars