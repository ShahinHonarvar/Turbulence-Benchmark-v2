def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(7, 10):
        num = numbers[i]
        if num % 2 == 0 or num % 3 == 0:
            total += num
    return total