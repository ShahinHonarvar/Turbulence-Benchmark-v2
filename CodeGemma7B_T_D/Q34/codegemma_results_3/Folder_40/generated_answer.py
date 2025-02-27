from functools import reduce 

def find_original_set(set1, set2):
    return reduce(lambda x, y: x.union(y), [set1, set2])