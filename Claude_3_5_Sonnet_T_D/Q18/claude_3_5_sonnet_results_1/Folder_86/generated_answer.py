def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(54, 80):
        if i < len(numbers):
            if numbers[i] % 54 == 0 or numbers[i] % 28 == 0:
                total += numbers[i]
    return total