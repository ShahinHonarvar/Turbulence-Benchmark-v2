def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 21 or len(list2) < 21:
        return set()
    return set(list1[20:31]).intersection(list2[20:31])