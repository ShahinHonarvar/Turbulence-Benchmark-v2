def find_original_set(set1: set[int], set2: set[int]) -> set[int]:
    if not set1.isdisjoint(set2):
        return set1.union(set2)
    return set1 | set2