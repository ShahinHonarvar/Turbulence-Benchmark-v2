def all_ints_div_by_both_two_nums(numbers):
    return [num for num in numbers[10:101] if num % 10 == 0 and num % 100 == 0]