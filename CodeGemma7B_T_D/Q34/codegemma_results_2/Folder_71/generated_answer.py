from itertools import combinations

def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16):
    all_sets = set()
    for subset in combinations(range(2 ** 16), r=16):
        test_set = set()
        for bit in range(16):
            if 1 << bit & subset:
                test_set.update(all_sets[bit])
        if set1.issubset(test_set) and set2.issubset(test_set) and set3.issubset(test_set) and set4.issubset(test_set) and set5.issubset(test_set) and set6.issubset(test_set) and set7.issubset(test_set) and set8.issubset(test_set) and set9.issubset(test_set) and set10.issubset(test_set) and set11.issubset(test_set) and set12.issubset(test_set) and set13.issubset(test_set) and set14.issubset(test_set) and set15.issubset(test_set) and set16.issubset(test_set):
            all_sets = test_set
    return all_sets