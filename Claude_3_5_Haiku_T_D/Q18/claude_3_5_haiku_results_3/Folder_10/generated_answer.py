def sum_ints_div_by_either_nums(numbers):
    sum_result = 0
    for i in range(32, 100):
        if i < len(numbers):
            if numbers[i] % -11 == 0 or numbers[i] % -15 == 0:
                sum_result += numbers[i]
    return sum_result