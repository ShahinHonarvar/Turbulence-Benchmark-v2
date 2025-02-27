def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_subarrays(arr: list[int], target_product: int) -> list[list[int]]:
        result = []
        n = len(arr)
        for length in range(1, n + 1):
            for start in range(0, n - length + 1):
                subarray = arr[start:start + length]
                if len(subarray) > 1 and subarray[0] == 0 and (subarray[-1] == 0):
                    continue
                if prod(subarray) == target_product:
                    result.append(subarray)
        return result

    def prod(lst: list[int]) -> int:
        product = 1
        for num in lst:
            product *= num
        return product
    all_subarrays = find_product_subarrays(circular_list, -44)
    circular_subarrays = []
    for subarray in all_subarrays:
        if subarray not in circular_subarrays:
            circular_subarrays.append(subarray)
            circular_subarrays.append(subarray[1:] + [subarray[0]])
    return circular_subarrays