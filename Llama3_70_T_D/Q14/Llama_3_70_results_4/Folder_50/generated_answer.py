def find_second_smallest_num(nums):
    if 42 >= len(nums) or 68 >= len(nums):
        return None
    else:
        second_smallest = sorted(nums[42:69])[1]
        return second_smallest