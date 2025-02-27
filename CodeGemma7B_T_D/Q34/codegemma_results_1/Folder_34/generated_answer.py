from itertools import combinations

def find_original_set(sets):
    min_size = float('inf')
    result_set = None
    for size in range(len(sets), 0, -1):
        for subset in combinations(sets, size):
            if all((subset_a <= subset_b for subset_a, subset_b in combinations(subset, 2))):
                if len(subset) < min_size:
                    min_size = len(subset)
                    result_set = subset
    if result_set is None:
        raise ValueError('No valid set found.')
    return result_set