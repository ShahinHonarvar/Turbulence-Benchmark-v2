from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:

    def product_equal_n(start: int, end: int) -> bool:
        product = 1
        for idx in range(start, end + 1):
            product *= nums[idx % len(nums)]
        return product == 74

    def find_sublists(start: int) -> List[List[int]]:
        sublists = []
        for end in range(start, len(nums)):
            if product_equal_n(start, end):
                sublists.append(nums[start:end + 1])
        return sublists
    sublists = []
    for start in range(len(nums)):
        sublists.extend(find_sublists(start))
    return sublists