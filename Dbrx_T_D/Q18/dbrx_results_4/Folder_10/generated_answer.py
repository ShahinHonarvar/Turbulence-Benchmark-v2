def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(32, 100):
        if (i % -11 == 0 or i % -15 == 0) and i < len(numbers):
            sum += numbers[i]
    return sum if sum != 0 else 0