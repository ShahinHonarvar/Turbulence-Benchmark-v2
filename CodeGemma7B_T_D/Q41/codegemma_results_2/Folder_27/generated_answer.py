import itertools # itertools.product()

def identical_elements(list1, list2):
    list1_range = range(66, 94)
    list2_range = range(66, 94)
    common_elements = set()
    for i1, i2 in itertools.product(list1_range, list2_range):
        if list1[i1] == list2[i2]:
            common_elements.add(list1[i1])
    return common_elements