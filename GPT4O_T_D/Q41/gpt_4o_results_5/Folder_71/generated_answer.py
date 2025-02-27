def identical_elements(list1, list2):
    start_idx = 26
    end_idx = 52
    sub1 = set(list1[start_idx:end_idx + 1])
    sub2 = set(list2[start_idx:end_idx + 1])
    return sub1 & sub2