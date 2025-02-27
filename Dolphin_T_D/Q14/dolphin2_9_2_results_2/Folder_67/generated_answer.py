def find_second_smallest_num(nums):
    sublist = nums[50:55]
    unique_nums = list(set(sublist))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    else:
        return unique_nums[1]