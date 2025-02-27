def return_nth_smallest_ascii(string):
    sub_string = string[20:81]
    sorted_sub_string = sorted(sub_string, key=lambda x: ord(x))
    return sorted_sub_string[10]