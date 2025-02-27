from itertools import combinations, chain

def find_original_set(*args):
    combined_sets = set(chain(*args))
    while True:
        new_sets = []
        for subset in combinations(combined_sets, len(combined_sets) - 1):
            if all((all((i in subset for i in arg_set)) for arg_set in args)):
                new_sets.append(subset)
        if len(new_sets) > 0:
            combined_sets = min(new_sets)
        else:
            break
    return combined_sets