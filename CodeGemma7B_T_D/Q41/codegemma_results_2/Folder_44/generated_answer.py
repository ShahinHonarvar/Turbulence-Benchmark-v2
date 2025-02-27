def identical_elements(list_one, list_two):
    if len(list_one) != len(list_two) or len(list_two) <= 13 or len(list_two) >= 68:
        return set()
    else:
        set_one = set(list_one[13:69])
        set_two = set(list_two[13:69])
        return set_one.intersection(set_two)