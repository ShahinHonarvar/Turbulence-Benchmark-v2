def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    def find_subarrays(lst, target_product):
        length = len(lst)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                subarray = lst[start:start + size]
                if product(subarray) == target_product:
                    result.append(subarray)
        return result
    all_subarrays = find_subarrays(circular_list, 42)
    unique_subarrays = [list(x) for x in set((tuple(x) for x in all_subarrays))]
    return unique_subarrays