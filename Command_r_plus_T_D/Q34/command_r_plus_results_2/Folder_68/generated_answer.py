def find_original_set(set1: set[int], set2: set[int], set3: set[int]) -> set[int]:
    union_set = set1.union(set2, set3)
    return union_set