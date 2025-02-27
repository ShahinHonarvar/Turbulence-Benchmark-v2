def return_nth_smallest_ascii(string):
    return sorted(string[0:8], key=ord)[-1]