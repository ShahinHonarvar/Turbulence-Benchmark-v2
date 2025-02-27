def all_ints_not_div_by_num(numbers):
    if len(numbers) < 97:
        return []
    return [num for num in numbers[91:97] if num % 13 != 0]