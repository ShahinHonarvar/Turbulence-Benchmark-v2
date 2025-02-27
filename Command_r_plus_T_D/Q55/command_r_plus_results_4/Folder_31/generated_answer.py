def lists_with_product_equal_n(nums: list[int]) -> list[list[int]]:

    def get_product(nums: list[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        return product

    def find_subarrays(nums: list[int], target_product: int) -> list[list[int]]:
        length = len(nums)
        subarrays = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                subarray = nums[start:start + size]
                if get_product(subarray) == target_product:
                    subarrays.append(subarray)
        return subarrays
    sublists = find_subarrays(nums, -16)
    return sublists