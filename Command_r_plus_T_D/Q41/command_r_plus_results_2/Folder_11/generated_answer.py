def identical_elements(list1, list2):
    common_elements = set()
    for i in range(37, min(52, len(list1))):
        if list1[i] in list2[i - 37:i - 37 + len(list1[i:])]:
            common_elements.add(list1[i])
    return common_elements