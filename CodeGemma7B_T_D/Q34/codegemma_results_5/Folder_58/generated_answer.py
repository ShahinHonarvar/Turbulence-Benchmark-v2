from itertools import combinations

def find_original_set(sets):
    min_set = set()
    for i in range(len(sets), 0, -1):
        for subset in combinations(sets, i):
            union_set = set()
            for s in subset:
                union_set.update(s)
            if union_set == min_set:
                return min_set
            elif union_set < min_set or not min_set:
                min_set = union_set