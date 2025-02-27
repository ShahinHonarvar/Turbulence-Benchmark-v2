def return_nth_smallest_ascii(string):
    sub_string = string[5:48]
    sorted_sub_string = sorted(sub_string, key=ord)
    return sorted_sub_string[12]