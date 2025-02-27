def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20):
    result_set = set1.copy()
    for i in range(2, 21):
        result_set.update(eval(f'set{i}'))
    return result_set