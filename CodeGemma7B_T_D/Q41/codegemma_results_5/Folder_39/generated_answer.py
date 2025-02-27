def identical_elements(list_one, list_two):
    result = set()
    for index in range(20, 31):
        if list_one[index] == list_two[index]:
            result.add(list_one[index])
    return result