def find_second_largest_num(nums):
    if len(nums) <= 200 and len(nums) >= 80:
        sublist = nums[80:201]
        if len(set(sublist)) >= 2:
            unique_nums = sorted(set(sublist))
            return unique_nums[-2]
    return None