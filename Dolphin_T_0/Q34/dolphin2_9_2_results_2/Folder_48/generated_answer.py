def combine_sets(*sets):
    combined_set = sets[0]
    for s in sets[1:]:
        combined_set = combined_set.union(s)
    return combined_set

def find_original_set(*args):
    return combine_sets(*args)