def identical_elements(list_one, list_two):
    new_set = set()
    for i in range(19, 93):
        if list_one[i] == list_two[i]:
            new_set.add(list_one[i])
    return new_set