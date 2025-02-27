def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(10, 80):
        if (i % -74 == 0 or i % -58 == 0) and i < len(numbers):
            sum += numbers[i]
    return sum if sum != 0 else 0