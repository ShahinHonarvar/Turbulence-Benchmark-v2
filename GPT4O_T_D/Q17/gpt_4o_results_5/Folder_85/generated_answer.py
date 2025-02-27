def all_ints_div_by_both_two_nums(integers):
    result = [num for num in integers[1:9] if num % 9 == 0 and num % 3 == 0]
    return result