def return_nth_smallest_ascii(string):
    sub_string = string[0:70]
    sorted_string = sorted(set(sub_string), key=lambda c: ord(c))
    return sorted_string[9]