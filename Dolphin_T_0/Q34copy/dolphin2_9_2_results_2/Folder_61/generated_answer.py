def find_original_set(set1, set2, set3, set4):
    if not set1.issubset(set2) and (not set2.issubset(set1)) and (not set1.issubset(set3)) and (not set3.issubset(set1)) and (not set1.issubset(set4)) and (not set4.issubset(set1)) and (not set2.issubset(set3)) and (not set3.issubset(set2)) and (not set2.issubset(set4)) and (not set4.issubset(set2)) and (not set3.issubset(set4)) and (not set4.issubset(set3)):
        new_set = set1.union(set2).union(set3).union(set4)
        return new_set
    else:
        return 'The sets are not distinct'