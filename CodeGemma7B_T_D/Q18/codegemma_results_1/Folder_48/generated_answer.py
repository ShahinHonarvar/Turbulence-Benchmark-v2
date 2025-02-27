def sum_ints_div_by_either_nums(nums):
    intIDS = [i for i in range(306, 958) if nums[i] % 982 == 0 or nums[i] % 319 == 0]
    if len(intIDS) == 0:
        return 0
    else:
        filtered_list = [nums[i] for i in intIDS]
        return sum(filtered_list)