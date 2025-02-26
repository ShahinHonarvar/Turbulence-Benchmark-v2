def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 10:
        return 0
    total = 0
    for num in numbers[6:10]:
        if num % -1 == 0 or num % -10 == 0:
            total += num
    return total