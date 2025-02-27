def all_ints_div_by_both_two_nums(nums):
    new_list = []
    for num in nums[7:9 + 1]:
        if num % 2 == 0 and num % 3 == 0:
            new_list.append(num)
    return new_list