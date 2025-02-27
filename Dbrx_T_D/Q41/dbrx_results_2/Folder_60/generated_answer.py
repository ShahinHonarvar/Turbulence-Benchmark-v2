def identical_elements(list1, list2):
    intersection = set()
    for i in range(len(list1)):
        if 75 <= i <= 85 and list1[i] == list2[i]:
            intersection.add(list1[i])
    return intersection