def sum_ints_div_by_either_nums(numbers):
    required = 0
    for i in range(22, 24 + 1):
        if numbers[i] % 85 == 0 or numbers[i] % 30 == 0:
            required += numbers[i]
    return required