def all_ints_not_div_by_num(numbers):
    return [num for i, num in enumerate(numbers[38:81]) if num % 49 != 0]