def identical_elements(list1: list, list2: list) -> set[int]:
    result = set()
    for i in range(70, 85):
        if list1[i] == list2[i]:
            result.add(list1[i])
    return result or set()