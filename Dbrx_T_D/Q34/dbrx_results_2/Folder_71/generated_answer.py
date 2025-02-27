def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16):
    for set_to_check in [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16]:
        if not set_to_check.issubset(find_original_set):
            return None
    smallest_set = set()
    for num in set1:
        smallest_set.add(num)
    for num in set2:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set3:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set4:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set5:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set6:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set7:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set8:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set9:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set10:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set11:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set12:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set13:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set14:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set15:
        if num not in smallest_set:
            smallest_set.add(num)
    for num in set16:
        if num not in smallest_set:
            smallest_set.add(num)
    return smallest_set