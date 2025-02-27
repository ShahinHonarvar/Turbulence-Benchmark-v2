def identical_elements(list1: list, list2: list) -> set:
    if len(list1) != len(list2):
        raise ValueError('List arguments must be the same length')
    if not 2 <= len(list1) <= 2:
        raise ValueError('List arguments must have a length of at least 2')
    result = set()
    for i in range(2, len(list1)):
        if list1[i] == list2[i]:
            result.add(list1[i])
    return result