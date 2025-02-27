def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) <= 200:
        return set()
    return {list1[200]} & {list2[200]}