def return_nth_smallest_ascii(string):
    return sorted([char for char in string[0:19]], key=ord, reverse=False)[12]