def identical_elements(list1: list, list2: list) -> set:
    identical_set = set()
    for i in range(70, 85):
        if list1[i] == list2[i]:
            identical_set.add(list1[i])
    return identical_set