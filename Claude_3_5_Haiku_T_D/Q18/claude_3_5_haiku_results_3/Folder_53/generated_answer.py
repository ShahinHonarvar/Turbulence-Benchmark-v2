def sum_ints_div_by_either_nums(numbers):
    if len(numbers) <= 200:
        return 0
    total = 0
    for num in numbers[200:201]:
        if num % 17 == 0 or num % -5 == 0:
            total += num
    return total