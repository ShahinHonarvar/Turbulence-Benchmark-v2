from functools import reduce

def return_nth_smallest_ascii(string):

    def get_ascii_value(ch):
        return ord(ch)
    return string[reduce(lambda x, y: x if get_ascii_value(x) < get_ascii_value(y) else y, string[17:84])]