def return_n_smallest_chars(s):
    sorted_characters = sorted(s, key=lambda x: ord(x))
    return_list = sorted_characters[:43]
    return_list.sort(reverse=True)
    return return_list