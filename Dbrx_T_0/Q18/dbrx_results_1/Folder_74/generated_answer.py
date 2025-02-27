def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(90, 98):
        num = numbers[i]
        if num % 13 == 0 or num % 35 == 0:
            total += num
    return total