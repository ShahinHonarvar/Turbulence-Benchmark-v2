def return_n_smallest_chars(s):
    return_list = []
    for i in range(49):
        smallest = min(s)
        s = s.replace(smallest, '')
        return_list.append(smallest)
    return_list.sort()
    return return_list