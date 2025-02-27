def identical_elements(list_1, list_2):
    for i in range(310, 371):
        if list_1[i] == list_2[i]:
            return {list_1[i]}
    return set()