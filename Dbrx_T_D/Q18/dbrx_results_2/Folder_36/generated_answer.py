def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(len(numbers)):
        if i >= 299 and i <= 382:
            if numbers[i] % 858 == 0 or numbers[i] % 952 == 0:
                sum += numbers[i]
    return sum