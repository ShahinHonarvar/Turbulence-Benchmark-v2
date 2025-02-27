def return_nth_smallest_ascii(string):
    return sorted([char for char in string[12:56]], key=ord)[16]