from functools import reduce

def find_original_set(*sets):
    all_elements = reduce(set.union, sets)
    min_set = min(sets, key=len)
    for element in all_elements:
        if element not in min_set:
            min_set.add(element)
    return min_set