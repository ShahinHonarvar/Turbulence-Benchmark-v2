def find_second_smallest_num(nums):
    if not isinstance(nums, list) or not all((isinstance(i, (int, float)) for i in nums)):
        return None
    sublist = nums[30:73] if len(nums) > 72 else nums
    if len(sublist) < 2:
        return None
    sublist.sort()
    if len(set(sublist)) < 2:
        return None
    return sublist[1]