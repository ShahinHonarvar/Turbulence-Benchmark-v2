from itertools import combinations_with_replacement

def find_original_set(sets):
    for i in range(len(sets) + 1):
        for subset in combinations_with_replacement(sets, i):
            if all((s.issubset(union) for s in sets for union in subset)):
                return union