from functools import reduce

def find_original_set(sets):
    return reduce(lambda a, b: a & b, [set(range(i + 1)) for i in range(max((len(s) for s in sets)) + 1)])