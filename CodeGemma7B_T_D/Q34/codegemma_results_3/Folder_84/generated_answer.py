from functools import reduce

def find_original_set(sets):

    def intersection(s1, s2):
        return s1.intersection(s2)
    smallest_set = sets[0]
    for s in sets[1:]:
        smallest_set = smallest_set.intersection(s)
    return smallest_set