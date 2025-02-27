def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 21 or len(list2) < 21:
        return set()
    target_elements = set(list1[20:31]).intersection(set(list2[20:31]))
    return target_elements