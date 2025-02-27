def identical_elements(list1, list2):
    to_return = set()
    for i in range(4, 5):
        if list1[i] in list2[i]:
            to_return.add(list1[i])
    return to_return