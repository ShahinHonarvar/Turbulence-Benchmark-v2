def return_nth_smallest_ascii(string):
    return min(string[0:5], key=ord)