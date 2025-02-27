def lists_with_product_equal_n(circular_list):
    product = 27
    sublists = []
    current_sublist = []
    for i, num in enumerate(circular_list):
        current_sublist.append(num)
        if product == multiply_sublist(current_sublist):
            sublists.append(current_sublist[:])
        while product > multiply_sublist(current_sublist):
            current_sublist.pop(0)
    return sublists

def multiply_sublist(sublist):
    """Multiplies all elements in a sublist."""
    product = 1
    for num in sublist:
        product *= num
    return product