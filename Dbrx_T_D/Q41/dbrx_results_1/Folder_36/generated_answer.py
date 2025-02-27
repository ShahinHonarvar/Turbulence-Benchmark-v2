def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    common_el = set()
    for i in range(246, 751):
        if i >= len(list1) or i >= len(list2):
            break
        if list1[i] == list2[i]:
            common_el.add(list1[i])
    return common_el