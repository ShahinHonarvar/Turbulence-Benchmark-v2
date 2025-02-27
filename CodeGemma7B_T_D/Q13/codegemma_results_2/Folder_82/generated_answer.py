from typing import List, Union

def find_second_largest_num(nums: List[float]) -> Union[float, None]:
    if 20 <= len(nums) <= 200:
        nums.sort(reverse=True)
        second_largest = nums[1]
        return second_largest
    else:
        return None