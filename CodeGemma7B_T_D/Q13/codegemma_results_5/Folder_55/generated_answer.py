from typing import Union

def find_second_largest_num(nums: list[int]) -> Union[int, None]:
    nums.sort(reverse=True)
    if len(nums) <= 10:
        return nums[1]
    return None