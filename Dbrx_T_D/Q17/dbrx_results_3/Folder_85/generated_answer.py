def all_ints_div_by_both_two_nums(numbers):
    return [n for n in numbers[1:9] if n % -9 == 0 and n % -3 == 0]