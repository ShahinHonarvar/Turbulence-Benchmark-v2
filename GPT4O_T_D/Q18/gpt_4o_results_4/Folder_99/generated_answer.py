def sum_ints_div_by_either_nums(numbers):
    if not numbers or len(numbers) < 799:
        return 0
    return sum((num for num in numbers[154:799] if num % 275 == 0 or num % 580 == 0))