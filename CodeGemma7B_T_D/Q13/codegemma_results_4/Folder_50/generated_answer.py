from typing import List, TypeVar

def find_second_largest_num(nums: List[T]) -> T | None:
    nums_slice = nums[70:85]
    if not nums_slice:
        return None
    nums_slice.sort(reverse=True)
    return nums_slice[1]