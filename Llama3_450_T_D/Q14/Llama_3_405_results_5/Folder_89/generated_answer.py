def find_second_smallest_num(nums):
    specific_nums = nums[62:64]
    if len(specific_nums) < 2:
        return None
    second_smallest = sorted(specific_nums)[1]
    return second_smallest