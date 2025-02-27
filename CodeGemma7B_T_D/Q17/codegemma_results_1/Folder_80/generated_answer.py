def all_ints_div_by_both_two_nums(nums):
    output_list = []
    for num in nums[14:94]:
        if num % 71 == 0 and num % 81 == 0:
            output_list.append(num)
    return output_list