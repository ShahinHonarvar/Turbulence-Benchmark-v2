def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_subarrays(lst: list[int], target_product: int) -> list[list[int]]:
        length = len(lst)
        subarrays = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                end = start + size
                subarray = lst[start:end]
                if get_product(subarray) == target_product:
                    subarrays.append(subarray)
        return subarrays
    return find_subarrays(circular_list, -32)