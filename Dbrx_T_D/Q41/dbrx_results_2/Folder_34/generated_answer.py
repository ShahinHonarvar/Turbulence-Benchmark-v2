def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 60 or len(list1) > 200:
        return set()
    else:
        return set(list1[59:200]) & set(list2[59:200])