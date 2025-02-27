def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(80, 201):
        num = numbers[i]
        if num % 10 == 0 or num % 1000 == 0:
            total += num
    return total