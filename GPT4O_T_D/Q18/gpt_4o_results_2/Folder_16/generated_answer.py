def sum_ints_div_by_either_nums(numbers):
    if not isinstance(numbers, list) or len(numbers) < 81:
        return 0
    return sum((num for num in numbers[55:81] if num % 22 == 0 or num % 32 == 0))