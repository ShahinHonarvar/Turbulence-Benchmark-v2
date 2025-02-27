def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists should have the same size')
    s1, s2 = (set(), set())
    for i in range(56, 83):
        if i < len(list1):
            s1.add(list1[i])
            s2.add(list2[i])
    return s1.intersection(s2)