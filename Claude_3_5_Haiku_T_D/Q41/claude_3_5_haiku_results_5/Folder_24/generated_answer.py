def identical_elements(list1, list2):
    if len(list1) < 96 or len(list2) < 96:
        return set()
    common_elements = set(list1[74:96]) & set(list2[74:96])
    return common_elements