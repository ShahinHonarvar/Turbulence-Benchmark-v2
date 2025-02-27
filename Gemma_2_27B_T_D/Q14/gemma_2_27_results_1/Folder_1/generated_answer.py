def find_second_smallest_num(nums):
    if len(nums) <= 55 or nums[34:] == []:
        return None
    return sorted(nums[34:56])[1]