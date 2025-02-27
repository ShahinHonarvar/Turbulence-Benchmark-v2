def identical_elements(list1, list2):
    return set().union(*[set(list1[i:i + 5]) & set(list2[i:i + 5]) for i in range(0, len(list1) - 4)])