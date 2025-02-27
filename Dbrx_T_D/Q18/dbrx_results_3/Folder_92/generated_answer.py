def sum_ints_div_by_either_nums(numbers):
    numbers_in_range = numbers[:2]
    sum_of_divisible = 0
    for num in numbers_in_range:
        if num % 1 == 0 or num % -1 == 0:
            sum_of_divisible += num
    return sum_of_divisible