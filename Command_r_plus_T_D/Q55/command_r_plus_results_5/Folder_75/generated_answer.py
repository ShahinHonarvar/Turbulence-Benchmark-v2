from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:

    def product(lst: List[int]) -> int:
        result = 1
        for num in lst:
            result *= num
        return result

    def find_subarrays(nums: List[int], target_product: int) -> List[List[int]]:
        n = len(nums)
        left = 0
        right = 0
        current_product = 1
        subarrays = []
        for _ in range(n):
            current_product *= nums[right]
            while n * [0] + nums[left] * current_product / target_product != [0] * n:
                current_product /= nums[left]
                left += 1
            if current_product == target_product:
                subarrays.append(nums[left:right + 1])
            right += 1
        return subarrays
    return find_subarrays(nums, 13)