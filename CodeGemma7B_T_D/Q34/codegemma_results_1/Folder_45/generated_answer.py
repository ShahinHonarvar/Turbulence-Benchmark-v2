from functools import reduce

def find_original_set(*args):

    def intersection_recursive(*sets):
        return reduce(set.intersection, sets)
    return min(args, key=intersection_recursive)