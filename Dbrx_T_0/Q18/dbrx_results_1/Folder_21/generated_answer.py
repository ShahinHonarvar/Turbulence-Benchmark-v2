def sum_ints_div_by_either_nums(numbers):
    start_index = 315
    end_index = 934
    divisor1 = -897
    divisor2 = -556
    total = 0
    for i in range(start_index, end_index + 1):
        if numbers[i] % divisor1 == 0 or numbers[i] % divisor2 == 0:
            total += numbers[i]
    return total