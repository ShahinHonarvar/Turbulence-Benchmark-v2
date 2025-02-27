def lists_with_product_equal_n(circular_list):

    def get_sublist_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = []
            product = 1
            for offset in range(size):
                current_index = (start + offset) % n
                sublist.append(circular_list[current_index])
                product *= circular_list[current_index]
                if product == 47:
                    result.append(sublist.copy())
                if product == 0 or product > 47:
                    break
    return result