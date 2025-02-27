def find_second_smallest_num(nums):
    if 661 <= len(nums) <= 924:
        sorted_nums = sorted(nums[661:925])
        if len(sorted_nums) > 1:
            return sorted_nums[1]
    return None