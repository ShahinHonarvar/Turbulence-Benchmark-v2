def find_second_smallest_num(nums):
    if len(nums) < 924 or 661 > len(nums):
        return None
    sliced_nums = nums[661:925]
    if len(sliced_nums) < 2:
        return None
    return sorted(sliced_nums)[1]