def return_nth_smallest_ascii(my_string):
    sub_string = my_string[12:87]
    sorted_sub_string = sorted(sub_string, key=lambda c: ord(c))
    return sorted_sub_string[16]