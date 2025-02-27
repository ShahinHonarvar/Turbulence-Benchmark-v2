def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(55, 67):
        if i < len(numbers):
            if numbers[i] % 22 == 0 or numbers[i] % 82 == 0:
                sum += numbers[i]
    return sum