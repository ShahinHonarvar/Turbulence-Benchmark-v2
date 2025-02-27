def return_n_smallest_chars(s):
    return_list = []
    sorted_chars = sorted(s, key=lambda x: ord(x))
    for i in range(20):
        return_list.append(sorted_chars[i])
    return return_list