def all_ints_div_by_num(numbers):
    if len(numbers) <= 10:
        return []
    return [num for num in numbers[10:11] if num % 1 == 0]