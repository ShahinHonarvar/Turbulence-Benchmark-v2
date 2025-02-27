def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21):
    sets = [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21]
    original_set = None
    for s in sets:
        count = 0
        for set in sets:
            if s.issubset(set):
                count += 1
        if count == len(sets):
            original_set = s
            break
    return original_set