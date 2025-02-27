def return_nth_smallest_ascii(string):
    return min(string[1:32], key=ord)