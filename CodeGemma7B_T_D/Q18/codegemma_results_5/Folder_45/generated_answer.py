def sum_ints_div_by_either_nums(numbers):
    count = 0
    for i in range(30, 201):
        if numbers[i] % -115 == 0 or numbers[i] % 115 == 0:
            count += numbers[i]
    return count