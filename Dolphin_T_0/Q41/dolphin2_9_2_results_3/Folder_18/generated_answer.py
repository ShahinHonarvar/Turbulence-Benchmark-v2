def identical_elements(list1, list2):
    output_set = set()
    for i in range(35, 50):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                output_set.add(list1[i])
    return output_set