def all_ints_div_by_both_two_nums(nums_list):
    evens = []
    nums_list = nums_list[138:425]
    for num in nums_list:
        if num % 863 == 0 and num % 329 == 0:
            evens.append(num)
    return evens