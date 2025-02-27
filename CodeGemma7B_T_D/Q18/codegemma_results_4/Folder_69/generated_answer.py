def sum_ints_div_by_either_nums(nums):
    indices = [idx for idx in range(61, 89) if nums[idx] % 31 == 0 or nums[idx] % 11 == 0]
    return sum(nums[indices]) if indices else 0