def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21, set22, set23):
    min_set = set()
    for s in [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21, set22, set23]:
        if not min_set or s < min_set:
            min_set = s
    return min_set