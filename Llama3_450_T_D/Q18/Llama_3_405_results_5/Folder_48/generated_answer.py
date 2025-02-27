def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers) if 306 <= i <= 957 and (num % 982 == 0 or num % 319 == 0)))