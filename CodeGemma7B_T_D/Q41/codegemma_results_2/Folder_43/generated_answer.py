def identical_elements(list1, list2):
    set2 = set(list2[68:87])
    i = 68
    while i <= 86:
        if list1[i] in set2:
            return {list1[i]}
        i += 1
    return set()