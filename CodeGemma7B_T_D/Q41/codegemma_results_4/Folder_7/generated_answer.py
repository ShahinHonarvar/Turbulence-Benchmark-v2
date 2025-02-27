def identical_elements(lst1, lst2):
    set_common = set()
    for i in range(661, 925):
        if lst1[i] in lst2[i]:
            set_common.add(lst1[i])
    return set_common