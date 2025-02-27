def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    second_smallest = sorted(nums[6:9])[1]
    return second_smallest