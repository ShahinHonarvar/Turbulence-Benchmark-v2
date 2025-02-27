def return_nth_smallest_ascii(string):
    return sorted([x for x in string[0:5]], key=ord)[4]