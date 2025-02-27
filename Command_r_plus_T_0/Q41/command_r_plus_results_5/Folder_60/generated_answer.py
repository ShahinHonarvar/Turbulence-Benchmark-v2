def identical_elements(list1: list, list2: list) -> set:
    common_elements = set()
    for i in range(75, min(86, len(list1))):
        if list1[i] in list2[i:i + 10]:
            common_elements.add(list1[i])
    return common_elements