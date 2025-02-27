def find_original_set(set1, set2):
    if set1.issubset(set2):
        return set2
    elif set2.issubset(set1):
        return set1
    else:
        return set1.union(set2)