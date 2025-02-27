def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    intersection = set()
    for i in range(len(list1)):
        if list1[i] == list2[i] and 90 <= i <= 200:
            intersection.add(list1[i])
    return intersection