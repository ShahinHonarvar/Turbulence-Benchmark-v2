def identical_elements(list1, list2):
    elts = set()
    for i in range(27, 56):
        if list1[i] == list2[i]:
            elts.add(list1[i])
    return elts