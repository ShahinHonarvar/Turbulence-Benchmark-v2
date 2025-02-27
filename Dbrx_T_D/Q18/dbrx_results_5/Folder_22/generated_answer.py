def sum_ints_div_by_either_nums(numbers):
    divisible_by_either = lambda num: num % 21 == 0 or num % 71 == 0
    return sum(filter(divisible_by_either, numbers[40:201]))