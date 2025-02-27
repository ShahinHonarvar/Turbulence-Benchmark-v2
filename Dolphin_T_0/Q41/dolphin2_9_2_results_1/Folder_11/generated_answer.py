def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    else:
        identical_elements = set()
        for i in range(37, 52):
            if i < len(list1):
                if list1[i] in list2:
                    identical_elements.add(list1[i])
        return identical_elements