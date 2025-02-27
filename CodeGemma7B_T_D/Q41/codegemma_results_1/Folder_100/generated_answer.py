def identical_elements(list_a, list_b):
    return {item for item in list_a[42:69] for item in list_b[42:69] if list_a[item] == list_b[item]}