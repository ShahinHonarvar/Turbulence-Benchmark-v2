def identical_elements(list1: list, list2: list) -> set:
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size.')
    if len(list1) < 606 or len(list2) < 606:
        raise ValueError('Both lists must have a size greater than or equal to 606.')
    common_elements = set()
    for i in range(533, 606):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    return common_elements