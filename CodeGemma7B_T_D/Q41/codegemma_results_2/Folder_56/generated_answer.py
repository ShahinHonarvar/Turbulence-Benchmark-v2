def identical_elements(old_list, new_list):
    identical_set = set()
    for i in range(1, 9):
        if old_list[i] == new_list[i]:
            identical_set.add(old_list[i])
    return identical_set