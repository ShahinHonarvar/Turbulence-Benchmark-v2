def find_second_smallest_num(nums):
    sliced_nums = nums[661:925]
    if len(sliced_nums) < 2:
        return None
    return sorted(sliced_nums)[1]