def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16, set17, set18, set19, set20, set21, set22, set23, set24, set25, set26, set27, set28):
    result = set()
    for i in range(len(locals())):
        for num in locals()['set' + str(i + 1)]:
            result.add(num)
    return result