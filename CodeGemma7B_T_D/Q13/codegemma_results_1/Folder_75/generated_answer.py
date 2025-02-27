from itertools import islice

def find_second_largest_num(l):
    if len(l) < 2:
        return None
    return next(islice(sorted(l, reverse=True), 56, 59))