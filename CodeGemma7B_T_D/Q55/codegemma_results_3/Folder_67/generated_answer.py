def lists_with_product_equal_n(array):
    full_product = 1
    for num in array:
        full_product *= num

    def helper(index, product, current_list):
        if index >= len(array):
            return [current_list]
        if product * array[index] == full_product:
            return [[*current_list, array[index]]] + helper(index + 1, 1, [])
        return helper(index + 1, product * array[index], current_list + [array[index]])
    return helper(0, 1, [])