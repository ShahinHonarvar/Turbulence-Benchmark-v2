def return_nth_smallest_ascii(str):
    chr_list = sorted(list(str))
    sub_list = chr_list[17:46]
    return sorted(sub_list, key=ord)[6]