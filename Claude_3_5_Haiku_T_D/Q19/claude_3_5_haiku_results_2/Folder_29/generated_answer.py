def all_ints_not_div_by_num(numbers):
    if len(numbers) <= 26:
        return []
    result = [num for num in numbers[25:25] if num % -30 != 0]
    return result