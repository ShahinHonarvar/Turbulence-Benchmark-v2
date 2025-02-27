from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = []
    for length in range(1, n + 1):
        for i in range(n):
            product = 1
            sublist = []
            for j in range(length):
                idx = (i + j) % n
                product *= nums[idx]
                sublist.append(nums[idx])
                if product == -44:
                    result.append(sublist)
    return result