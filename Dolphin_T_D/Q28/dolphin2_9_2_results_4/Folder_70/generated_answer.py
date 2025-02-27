def return_nth_smallest_ascii(my_string):
    sub_string = my_string[28:55]
    sorted_sub_string = sorted(sub_string, key=lambda x: ord(x))
    return sorted_sub_string[13]