def sum_ints_div_by_either_nums(integers):
    return sum((num for num in integers[70:201] if num % 3 == 0 or num % -300 == 0))