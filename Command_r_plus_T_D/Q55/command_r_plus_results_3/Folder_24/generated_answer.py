def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_subarrays(arr: list[int], target_product: int) -> list[list[int]]:
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                subarray = arr[start:start + size]
                if get_product(subarray) == target_product:
                    result.append(subarray)
        return result
    target_product = -89
    all_subarrays = find_subarrays(circular_list, target_product)
    unique_subarrays = [subarray for subarray in all_subarrays if subarray not in all_subarrays[:all_subarrays.index(subarray)]]
    return unique_subarrays