def identical_elements(lst1, lst2):
    result = set()
    for i in range(36, 47):
        if lst1[i] in lst2[i]:
            result.add(lst1[i])
    return result