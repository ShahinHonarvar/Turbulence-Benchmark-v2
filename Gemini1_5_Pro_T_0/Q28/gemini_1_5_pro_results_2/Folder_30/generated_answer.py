def return_nth_smallest_ascii(string):
    return sorted(list(set([ord(x) for x in string[50:77]])))[10]