def lists_with_product_equal_n(values):

    def get_product(values):
        product = 1
        for v in values:
            product *= v
        return product
    sublists = []
    curr_values = []
    curr_product = 1
    for value in values + values:
        if curr_product == -30:
            sublists.append(curr_values[:])
        while curr_product <= -30:
            curr_product //= curr_values.pop(0)
        curr_values.append(value)
        curr_product *= value
    return sublists