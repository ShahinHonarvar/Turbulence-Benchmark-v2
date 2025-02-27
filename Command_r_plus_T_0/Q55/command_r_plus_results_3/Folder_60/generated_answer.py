def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                end = start + size - 1
                if arr[start] * arr[end] == target:
                    result.append(arr[start:end + 1])
        return result
    sublists = find_subarrays(circular_list, 49)
    sublists_with_product_49 = []
    for sublist in sublists:
        product = 1
        for num in sublist:
            product *= num
        if product == 49:
            sublists_with_product_49.append(sublist)
    return sublists_with_product_49