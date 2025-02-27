def identical_elements(list1, list2):
    index_start = 32
    index_end = 35
    if len(list1) <= index_end or len(list2) <= index_end:
        return set()
    sublist1 = list1[index_start:index_end + 1]
    sublist2 = list2[index_start:index_end + 1]
    return set(sublist1).intersection(sublist2)