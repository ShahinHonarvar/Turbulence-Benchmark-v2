def return_nth_smallest_ascii(string):
    return sorted([ord(char) for char in string[25:78]])[15]