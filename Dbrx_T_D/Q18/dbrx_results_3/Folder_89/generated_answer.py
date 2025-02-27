def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(len(numbers)):
        if i >= 28 and i <= 96:
            if numbers[i] % 90 == 0 or numbers[i] % 97 == 0:
                sum += numbers[i]
    return sum