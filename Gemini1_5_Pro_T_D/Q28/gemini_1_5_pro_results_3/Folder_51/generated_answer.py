def return_nth_smallest_ascii(string):
    return sorted(set([ord(x) for x in string[10:74]]))[8]