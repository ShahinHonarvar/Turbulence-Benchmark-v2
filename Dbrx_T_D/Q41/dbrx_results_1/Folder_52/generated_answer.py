def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return {list1[i] for i in range(28, 39) if list1[i] == list2[i]} & {list2[i] for i in range(28, 39) if list1[i] == list2[i]}