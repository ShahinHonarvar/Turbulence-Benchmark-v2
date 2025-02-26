def sum_ints_div_by_either_nums(numbers):
    total_sum = 0
    for i in range(154, 799):
        if i < len(numbers):
            if numbers[i] % 275 == 0 or numbers[i] % 580 == 0:
                total_sum += numbers[i]
    return total_sum