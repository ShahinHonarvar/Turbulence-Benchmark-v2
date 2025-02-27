def identical_elements(list_one, list_two):
    common_elements = set()
    for i in range(639, 976):
        if list_one[i] == list_two[i]:
            common_elements.add(list_one[i])
    return common_elements