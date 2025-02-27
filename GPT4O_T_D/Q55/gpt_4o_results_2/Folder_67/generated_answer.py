def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    size = len(circular_list)
    result = []
    for start in range(size):
        current_product = 1
        sublist = []
        for offset in range(size):
            index = (start + offset) % size
            current_product *= circular_list[index]
            sublist.append(circular_list[index])
            if current_product == 33:
                result.append(sublist.copy())
            if current_product == 0:
                break
    return result