def return_nth_smallest_ascii(string):
    return sorted([ord(x) for x in string[12:73]])[12]