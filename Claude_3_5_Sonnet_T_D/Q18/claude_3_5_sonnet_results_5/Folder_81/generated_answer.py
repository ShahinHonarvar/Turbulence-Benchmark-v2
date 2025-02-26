def sum_ints_div_by_either_nums(numbers):
    result = 0
    for i in range(10, min(101, len(numbers))):
        if numbers[i] % 10 == 0:
            result += numbers[i]
    return result