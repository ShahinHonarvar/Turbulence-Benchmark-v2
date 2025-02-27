def sum_ints_div_by_either_nums(numbers):
    if not isinstance(numbers, list) or len(numbers) < 97:
        return 0
    total = 0
    for i in range(28, 97):
        num = numbers[i]
        if num % 90 == 0 or num % 97 == 0:
            total += num
    return total