def all_ints_div_by_both_two_nums(numbers):
    divisible_by_72_and_70 = [num for num in numbers[69:71] if num % 72 == 0 and num % 70 == 0]
    return divisible_by_72_and_70