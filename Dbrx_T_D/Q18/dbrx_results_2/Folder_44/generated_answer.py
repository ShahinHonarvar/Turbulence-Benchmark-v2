def sum_ints_div_by_either_nums(numbers):
    divisible = lambda x: x % 74 == 0 or x % 15 == 0
    return sum(filter(divisible, numbers[25:71]))