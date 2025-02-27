def return_nth_smallest_ascii(string):
    sub_string = string[52:80]
    sorted_sub_string = sorted(sub_string, key=lambda x: Ord(x))
    return sorted_sub_string[6]