def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21, set22, set23, set24, set25, set26, set27, set28, set29, set30, set31, set32, set33, set34, set35, set36, set37, set38):
    all_sets = [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21, set22, set23, set24, set25, set26, set27, set28, set29, set30, set31, set32, set33, set34, set35, set36, set37, set38]
    original_set = set()
    for s in all_sets:
        original_set.update(s)
    return original_set