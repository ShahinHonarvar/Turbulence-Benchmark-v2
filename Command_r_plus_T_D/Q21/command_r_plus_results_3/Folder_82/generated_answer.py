def all_ints_div_by_num(numbers_list):
    divisible_by_3 = [num for num in numbers_list[:3] if num % 3 == 0]
    return divisible_by_3