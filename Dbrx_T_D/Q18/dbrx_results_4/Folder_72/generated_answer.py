def sum_ints_div_by_either_nums(numbers):
    nums_to_check = numbers[38:82]
    return sum((x for x in nums_to_check if x % -61 == 0 or x % -71 == 0))