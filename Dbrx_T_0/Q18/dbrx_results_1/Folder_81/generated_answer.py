def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(10, 101):
        if i >= len(numbers):
            break
        if numbers[i] % 10 == 0 or numbers[i] % 100 == 0:
            total += numbers[i]
    return total