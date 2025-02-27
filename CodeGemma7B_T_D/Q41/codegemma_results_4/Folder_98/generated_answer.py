def identical_elements(list_a, list_b):
    result = set()
    if len(list_a) == len(list_b) and len(list_a) <= 5:
        for i in range(len(list_a)):
            if list_a[i] in list_b[i] and i >= 0 and (i <= 5):
                result.add(list_a[i])
    return result