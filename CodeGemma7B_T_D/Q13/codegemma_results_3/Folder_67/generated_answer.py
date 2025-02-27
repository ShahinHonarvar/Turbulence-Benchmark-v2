from typing import Union

def find_second_largest_num(nums: list[int]) -> Union[int, str]:
    """
            Returns the second largest element from index 22 to index 50, both inclusive.
            If there is no such element, the function should return 'None'.
            """
    if not nums or len(nums) < 22 or len(nums) > 50:
        return 'None'
    nums.sort(reverse=True)
    return nums[21]