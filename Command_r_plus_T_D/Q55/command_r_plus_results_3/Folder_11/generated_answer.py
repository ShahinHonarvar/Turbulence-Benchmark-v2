def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, target_product, size):
        result = []
        for i in range(len(lst)):
            product = 1
            subarray = []
            for j in range(i, min(i + size, len(lst))):
                product *= lst[j]
                subarray.append(lst[j])
                if product == target_product:
                    result.append(subarray)
        return result
    sublists = []
    for size in range(1, len(circular_list) + 1):
        subarrays = find_subarrays(circular_list, -15, size)
        sublists.extend(subarrays)
    return sublists