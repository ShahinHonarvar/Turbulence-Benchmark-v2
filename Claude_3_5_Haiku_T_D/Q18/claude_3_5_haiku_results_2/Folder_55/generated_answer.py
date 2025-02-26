def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(min(10, len(numbers))):
        if numbers[i] % 10 == 0 or numbers[i] % 100 == 0:
            total += numbers[i]
    return total