def identical_elements(list1, list2):
    if not (all((isinstance(i, list) for i in [list1, list2])) and len(list1) == len(list2)):
        raise ValueError('Both arguments must be lists and of the same size.')
    target_indices = set(range(32, 36))
    common_elements = set()
    for i in target_indices:
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    return common_elements