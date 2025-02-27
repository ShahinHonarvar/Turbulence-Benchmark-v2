def identical_elements(list1, list2):
    for i in range(2, len(list1)):
        for j in range(2, len(list2)):
            if list1[i] == list2[j] and list1[i] not in set(list1[:2] + list1[i + 1:]) and (list2[j] not in set(list2[:2] + list2[j + 1:])):
                return {list1[i]}
    return set()