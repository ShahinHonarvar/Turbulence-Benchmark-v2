def lists_with_product_equal_n(circular_list):

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = 54
    result = []
    list_length = len(circular_list)
    for start_idx in range(list_length):
        product = 1
        for length in range(1, list_length + 1):
            end_idx = (start_idx + length) % list_length
            product *= circular_list[end_idx - 1]
            if product == n:
                if end_idx > start_idx:
                    sublist = circular_list[start_idx:end_idx]
                else:
                    sublist = circular_list[start_idx:] + circular_list[:end_idx]
                result.append(sublist)
            if end_idx == start_idx:
                break
            if product > n:
                break
    return result