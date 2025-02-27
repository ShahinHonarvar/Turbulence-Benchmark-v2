from typing import Set

def composite_nums_between_indices(nums: list) -> Set[int]:
    composite_nums: Set[int] = set()
    for i in range(68, 87):
        num = nums[i]
        if num != 1 and all((num % j != 0 for j in range(2, int(num ** 0.5) + 1))):
            composite_nums.add(num)
    return composite_nums