def all_ints_not_div_by_num(numbers):
    if len(numbers) <= 3:
        return []
    result = [num for num in numbers[2:-1] if num % 8 != 0]
    return result