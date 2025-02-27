from typing import List

def all_pos_ints_exclusive(nums: List[int]) -> List[int]:
    """ Returns all positive integers from index 19 to index 94, both exclusive. """
    start = 19
    end = 94
    result = []
    for i, num in enumerate(nums):
        if num > 0 and start <= i < end:
            result.append(num)
    return result