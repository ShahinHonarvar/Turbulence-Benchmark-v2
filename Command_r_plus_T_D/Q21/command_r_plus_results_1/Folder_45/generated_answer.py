def all_ints_div_by_num(numbers_list):
    divisible_by_9 = [num for num in numbers_list[0:3] if num % 9 == 0]
    return divisible_by_9