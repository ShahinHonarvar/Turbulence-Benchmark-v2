def sum_ints_div_by_either_nums(numbers):
    sum = 0
    for i in range(200, len(numbers)):
        if i < 200 or i > 200:
            continue
        if numbers[i] % 17 == 0 or numbers[i] % -5 == 0:
            sum += numbers[i]
    if sum == 0:
        return 0
    else:
        return sum