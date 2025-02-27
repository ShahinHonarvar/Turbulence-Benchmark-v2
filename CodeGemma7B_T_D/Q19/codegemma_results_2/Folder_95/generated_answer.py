def all_ints_not_div_by_num(nums):
    integers = nums[38:52]
    divisible_by_num = [i for i in integers if i % -41 == 0]
    integers = [i for i in integers if i not in divisible_by_num]
    return integers