def sum_ints_div_by_either_nums(numbers):
    total = 0
    start, end = (29, 45)
    for i in range(start, end + 1):
        if numbers[i] % 27 == 0 or numbers[i] % 81 == 0:
            total += numbers[i]
    return total if total > 0 else 0