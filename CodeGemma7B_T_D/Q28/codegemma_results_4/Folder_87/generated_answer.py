def return_nth_smallest_ascii(str):
    less_than_set = {ord(i) for i in str if ord(i) < ord(str[29])}
    greater_than_set = {ord(i) for i in str if ord(i) > ord(str[33])}
    mid_set = set(range(ord(str[29]), ord(str[33]) + 1)).difference(greater_than_set).difference(less_than_set)
    least_ascii_index = sorted(list(mid_set))[4]
    final_char = chr(least_ascii_index)
    return final_char