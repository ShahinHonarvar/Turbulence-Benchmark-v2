def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    def find_subarrays(lst, target_product):
        length = len(lst)
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                subarray = lst[start:start + size]
                if product(subarray) == target_product:
                    yield subarray
    result = []
    for sublist in find_subarrays(circular_list, 632):
        result.append(sublist)
    return result