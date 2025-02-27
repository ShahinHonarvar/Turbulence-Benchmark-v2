def identical_elements(list1, list2):
    index_set = set()
    for index in range(min(len(list1), len(list2))):
        if list1[index] == list2[index]:
            index_set.add(list1[index])
    return index_set

def identical_elements(list1, list2):
    return {list1[0]} if list1[0] == list2[0] else set()