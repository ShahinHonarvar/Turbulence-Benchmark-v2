def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)

    def find_sublist_product(start_index):
        sub_list = []
        product = 1
        for i in range(n):
            curr_index = (start_index + i) % n
            sub_list.append(circular_list[curr_index])
            product *= circular_list[curr_index]
            if product == -75:
                result.append(sub_list[:])
    for i in range(n):
        find_sublist_product(i)
    return result