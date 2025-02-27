def all_ints_div_by_num(numbers_list):
    divisible_by_6 = [num for num in numbers_list[:6] if num % 6 == 0]
    return divisible_by_6