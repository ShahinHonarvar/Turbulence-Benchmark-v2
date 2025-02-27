def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(6, 10):
        if i < 0 or i >= len(numbers):
            break
        if numbers[i] % -1 == 0 or numbers[i] % -10 == 0:
            sum += numbers[i]
    return sum