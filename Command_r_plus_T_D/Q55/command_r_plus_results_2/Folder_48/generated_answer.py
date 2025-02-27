def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_sublist_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_subarrays(nums: list[int], target: int) -> list[list[int]]:
        subarrays = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarray = nums[i:j + 1]
                if get_sublist_product(subarray) == target:
                    subarrays.append(subarray)
        return subarrays
    return find_subarrays(circular_list, 990)