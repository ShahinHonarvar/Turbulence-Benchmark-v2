def sum_ints_div_by_either_nums(numbers):
    start_index = 138
    end_index = 424
    divisor1 = -863
    divisor2 = -329
    total = 0
    for i in range(start_index, end_index + 1):
        if numbers[i] % divisor1 == 0 or numbers[i] % divisor2 == 0:
            total += numbers[i]
    return total