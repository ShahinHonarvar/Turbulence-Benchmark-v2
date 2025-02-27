def identical_elements(list1, list2):
    set1 = set()
    n = len(list1)
    for i in range(26, min(52, n)):
        for j in range(26, min(52, m)):
            if list1[i] == list2[j]:
                set1.add(list1[i])
    return set1