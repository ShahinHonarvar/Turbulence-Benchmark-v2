from typing import Union

def find_second_largest_num(nums: list) -> Union[int, str]:
    nums.sort(reverse=True)
    try:
        return nums[35:50][1]
    except IndexError:
        return 'None'