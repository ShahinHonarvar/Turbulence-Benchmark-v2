from itertools import product

def find_original_set(sets):
    original_set = set()
    for elements in product(*sets):
        new_set = set(elements)
        if all((s.issubset(new_set) for s in sets)):
            if not original_set or len(new_set) < len(original_set):
                original_set = new_set
    return original_set