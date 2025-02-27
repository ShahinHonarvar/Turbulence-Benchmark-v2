def identical_elements(list1, list2):
    result = set()
    idx1 = 246
    idx2 = 750
    if len(list1) == len(list2) and len(list1) >= 506:
        while idx1 <= idx2:
            if list1[idx1] in list2[idx2]:
                result.add(list1[idx1])
            idx1 += 1
            idx2 -= 1
    return result