def return_nth_smallest_ascii(string):
    return sorted([ord(s) for s in string])[4]