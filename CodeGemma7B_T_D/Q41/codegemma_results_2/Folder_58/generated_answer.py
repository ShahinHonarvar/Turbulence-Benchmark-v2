def identical_elements(l1, l2):
    result = set()
    for i in range(209, 557):
        if l1[i] == l2[i]:
            result.add(l1[i])
    return result