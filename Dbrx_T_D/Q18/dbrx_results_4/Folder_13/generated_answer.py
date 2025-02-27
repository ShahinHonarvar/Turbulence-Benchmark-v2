def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(13, 19):
        number = numbers[i]
        if number % 45 == 0 or number % 20 == 0:
            total += number
    return total