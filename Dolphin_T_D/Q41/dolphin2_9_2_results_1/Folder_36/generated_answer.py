def identical_elements(list1, list2):
    output = set()
    for i in range(246, 751):
        if list1[i] == list2[i]:
            output.add(list1[i])
    return output