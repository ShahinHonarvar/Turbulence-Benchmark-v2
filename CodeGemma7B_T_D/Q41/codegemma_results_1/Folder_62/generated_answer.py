def identical_elements(list_one, list_two):
    elements_in_both = set()
    if len(list_one) == len(list_two) and len(list_one) >= 91 and (len(list_two) >= 91):
        for i in range(91, 100):
            if list_one[i] == list_two[i]:
                elements_in_both.add(list_one[i])
    return elements_in_both