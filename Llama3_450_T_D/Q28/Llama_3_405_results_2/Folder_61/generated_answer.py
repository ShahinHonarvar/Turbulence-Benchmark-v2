def return_nth_smallest_ascii(s):
    sublist = s[:10]
    sorted_list = sorted(sublist, key=lambda x: ord(x))
    return sorted_list[9]