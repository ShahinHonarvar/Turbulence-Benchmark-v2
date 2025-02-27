def sum_ints_div_by_either_nums(numbers):
    total = 0
    for i, num in enumerate(numbers):
        if i >= 48 and i <= 59:
            if num % 88 == 0 or num % 58 == 0:
                total += num
    return total