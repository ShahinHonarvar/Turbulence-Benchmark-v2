from typing import List, Optional

def find_second_smallest_num(nums: List[int]) -> Optional[int]:
    """
    This function takes one argument, a list of distinct numbers, as input and returns the second smallest element from index 4 to index 4, both inclusive. If there is no such an element, the function should return 'None'.
    """
    nums = list(set(nums))
    nums.sort()
    if len(nums) < 5:
        return None
    return nums[4]