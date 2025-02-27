def find_n_th_smallest_num(nums):
    sub_nums = sorted(nums[45:83])
    if len(sub_nums) >= 15:
        return sub_nums[14]
    else:
        raise ValueError('Invalid input: Not enough numbers')