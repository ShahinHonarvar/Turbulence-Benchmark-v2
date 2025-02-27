def all_ints_div_by_both_two_nums(numbers):
    div_result = [num for num in numbers[10:77] if num % -40 == 0 and num % -12 == 0]
    return div_result