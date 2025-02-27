from functools import reduce

def return_nth_smallest_ascii(string):
    return reduce(lambda x, y: x if ord(x) < ord(y) else y, string[5:47 + 1])