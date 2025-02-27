def return_nth_smallest_ascii(string):
    sub_string = string[44:70]
    sorted_sub_string = sorted(sub_string, key=lambda c: ord(c))
    return sorted_sub_string[14]