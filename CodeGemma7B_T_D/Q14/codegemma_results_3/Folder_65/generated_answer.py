from typing import List, Optional

def find_second_smallest_num(nums: List[int]) -> Optional[int]:
    """
    Finds the second smallest element from index 56 to index 57, both inclusive. If there is
    no such an element, the function should return 'None'.

    Args:
      nums: A list of distinct numbers.

    Returns:
      The second smallest element from index 56 to index 57, both inclusive. If there is
      no such an element, the function should return 'None'.
    """
    if 56 < len(nums) <= 57:
        return None
    nums_five_six_to_five_seven = nums[56:58]
    second_smallest_num = float('inf')
    for num in nums_five_six_to_five_seven:
        if num < second_smallest_num:
            second_smallest_num = num
    return second_smallest_num if second_smallest_num != float('inf') else None