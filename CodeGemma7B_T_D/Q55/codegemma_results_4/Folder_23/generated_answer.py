def lists_with_product_equal_n(circular_list):
    """circular_list is a circular list of integers"""
    product = -95
    'product of the sublists should be equal to this'
    sublists = []
    'list of sublists'
    for i in range(len(circular_list)):
        'start of the sublist'
        multiplier = circular_list[i]
        'multiplier of the sublist'
        j = (i + 1) % len(circular_list)
        'end of the sublist'
        while multiplier * circular_list[j] == product:
            sublists.append(circular_list[i:j + 1])
            j = (j + 1) % len(circular_list)
    return sublists