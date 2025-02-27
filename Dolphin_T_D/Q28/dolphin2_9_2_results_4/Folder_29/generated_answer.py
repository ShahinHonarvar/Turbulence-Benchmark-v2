def return_nth_smallest_ascii(input_string):
    sub_string = list(input_string[5:11])
    sorted_string = sorted(sub_string, key=ord)
    return sorted_string[5]