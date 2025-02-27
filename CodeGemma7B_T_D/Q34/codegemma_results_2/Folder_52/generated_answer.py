from itertools import product

def find_original_set(sets):
    all_elements = set()
    for s in sets:
        all_elements.update(s)
    for size in range(len(sets[0]), len(all_elements) + 1):
        for subset in product(sets, repeat=size):
            test_set = set()
            for s in subset:
                test_set.update(s)
            if test_set == all_elements:
                return test_set