def identical_elements(list1, list2):
    results = set()
    for index in range(262, 747):
        if list1[index] == list2[index]:
            results.add(list1[index])
    return results