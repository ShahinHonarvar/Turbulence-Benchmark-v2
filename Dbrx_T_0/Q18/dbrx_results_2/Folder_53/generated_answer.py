def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i in range(200, 201):
        if i < 0 or i >= len(numbers):
            break
        num = numbers[i]
        if num % 17 == 0 or num % -5 == 0:
            total += num
    return total