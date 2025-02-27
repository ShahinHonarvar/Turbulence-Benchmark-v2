def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for i in range(n):
        current_list = []
        for j in range(n):
            current_index = (i + j) % n
            current_list.append(circular_list[current_index])
            if product_of_list(current_list) == -32:
                result.append(current_list[:])
    return result