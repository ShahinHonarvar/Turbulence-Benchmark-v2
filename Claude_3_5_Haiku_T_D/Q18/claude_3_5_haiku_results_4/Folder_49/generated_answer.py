def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 201:
        return 0
    return sum((num for num in numbers[80:201] if num % 10 == 0 or num % 1000 == 0))