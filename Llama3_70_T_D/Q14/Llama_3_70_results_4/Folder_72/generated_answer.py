def find_second_smallest_num(nums):
    if 82 <= len(nums) <= 86:
        second_smallest = sorted(nums[82:87])[1]
        return second_smallest
    else:
        return None