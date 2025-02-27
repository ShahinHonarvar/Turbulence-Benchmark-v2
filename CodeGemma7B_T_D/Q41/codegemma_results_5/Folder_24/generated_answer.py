def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b) or not (74 <= len(list_a) <= 95 and 74 <= len(list_b) <= 95):
        return set()
    return set(list_a[74:96]) & set(list_b[74:96])