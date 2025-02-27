def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9):
    result = set()
    for i in range(1, 10):
        temp_set = set()
        for j in range(i):
            temp_set.add(i * j + i)
        temp_set.update(set1)
        temp_set.update(set2)
        temp_test.update(set3)
        temp_test.update(set4)
        temp_test.update(set5)
        temp_test.update(set6)
        temp_test.update(set7)
        temp_test.update(set8)
        temp_test.update(set9)
        if all((temp.issubset(temp_set) for temp in [set1, set2, set3, set4, set5, set6, set7, set8, set9])):
            result = temp_set
            break
    return result