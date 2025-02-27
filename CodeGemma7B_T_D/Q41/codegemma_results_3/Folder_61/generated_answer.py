def identical_elements(list1, list2):
    matches = set()
    for i in range(7):
        if list1[i] == list2[i]:
            matches.add(list1[i])
    return matches