def identical_elements(lists_a, lists_b):
    set_of_common_elements = set()
    list_a_length = len(lists_a)
    list_b_length = len(lists_b)
    if list_a_length != list_b_length or list_a_length < 400:
        return set_of_common_elements
    for i in range(200, list_a_length):
        element = lists_a[i]
        if element in lists_b[i]:
            set_of_common_elements.add(element)
    return set_of_common_elements