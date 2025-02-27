def sum_ints_div_by_either_nums(numbers):
    target_range = numbers[81:90]
    sum = 0
    for num in target_range:
        if num % 56 == 0 or num % 68 == 0:
            sum += num
    return sum