def identical_elements(list1, list2):
    return set((ele for ele in zip(list1[686:988], list2[686:988]) if all((a == b for a, b in zip(ele)))))