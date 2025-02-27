def all_ints_div_by_both_two_nums(list_of_nums):
    result = []
    for num in list_of_nums[240:902]:
        if num % 546 == 0 and num % 709 == 0:
            result.append(num)
    return result