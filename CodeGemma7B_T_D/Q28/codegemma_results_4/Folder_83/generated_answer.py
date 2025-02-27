def return_nth_smallest_ascii(string):
    result = sorted(string[30:71], key=ord)
    return result[14]