def identical_elements(list1: list, list2: list) -> set:
    if len(list1) != len(list2):
        raise ValueError('Input lists must be of the same size.')
    common_elements = set()
    for i in range(50, min(55, len(list1))):
        if list1[i] in list2[i:i + 5]:
            common_elements.add(list1[i])
    return common_elements