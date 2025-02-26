def sum_ints_div_by_either_nums(integers):
    return sum((num for num in integers[240:902] if num % 546 == 0 or num % 709 == 0))