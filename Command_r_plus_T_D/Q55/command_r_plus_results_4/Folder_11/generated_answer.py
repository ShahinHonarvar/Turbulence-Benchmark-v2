from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:

    def product_equal_n(nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        result = []
        for size in range(1, length + 1):
            for start in range(length):
                sublist = nums[start:start + size]
                if len(sublist) == size and sublist[0] != 0 and (prod(sublist) == target):
                    result.append(sublist)
        return result

    def prod(nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        return product
    result = []
    for sublist in product_equal_n(nums, -15):
        result.append(sublist)
    for sublist in product_equal_n(nums, 15):
        result.append(list(reversed(sublist)))
    return result