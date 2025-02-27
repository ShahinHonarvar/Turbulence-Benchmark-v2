def lists_with_product_equal_n(circular_list):

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_subarrays(lst, product):
        length = len(lst)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                subarray = lst[start:start + size]
                if get_product(subarray) == product:
                    result.append(subarray)
        return result
    product_32_sublists = []
    for i in range(len(circular_list)):
        temp_list = circular_list[i:] + circular_list[:i]
        product_32_sublists.extend(find_subarrays(temp_list, 32))
    return product_32_sublists