def find_original_set(set1, set2, set3):
    result = set()
    for dat in set1:
        result.add(dat)
    for dat in set2:
        result.add(dat)
    for dat in set3:
        result.add(dat)
    return result