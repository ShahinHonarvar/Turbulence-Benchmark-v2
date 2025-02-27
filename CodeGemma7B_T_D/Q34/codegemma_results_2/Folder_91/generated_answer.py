def find_original_set(set1, set2, set3, set4, set5):
    result = set1 | set2 | set3 | set4 | set5
    for s in result:
        if s not in set1 or s not in set2 or s not in set3 or (s not in set4) or (s not in set5):
            result.remove(s)
    return result