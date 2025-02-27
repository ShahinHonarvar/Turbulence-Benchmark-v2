from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:

    def product(lst: List[int]) -> int:
        result = 1
        for num in lst:
            result *= num
        return result

    def generate_sublists(lst: List[int], size: int) -> List[List[int]]:
        return [lst[i:i + size] for i in range(len(lst) - size + 1)]

    def find_sublists_with_product(lst: List[int], target_product: int) -> List[List[int]]:
        sublists = []
        for size in range(1, len(lst) + 1):
            sublist_candidates = generate_sublists(lst, size)
            for sublist in sublist_candidates:
                if product(sublist) == target_product:
                    sublists.append(sublist)
        return sublists
    return find_sublists_with_product(nums, 74)