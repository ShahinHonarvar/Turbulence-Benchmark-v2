def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16):
    mini_set = set1
    for i in range(2, 17):
        if i == 2:
            mini_set = set1.union(set2)
        else:
            mini_set = mini_set.union(locals()['set' + str(i)])
    return mini_set