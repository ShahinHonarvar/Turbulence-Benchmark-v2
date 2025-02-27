def identical_elements(list_a, list_b):
    identical = set()
    for i in range(30, 87 + 1):
        if list_a[i] in list_b and list_b[i] in list_a:
            identical.add(list_a[i])
    return identical