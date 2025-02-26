def all_ints_div_by_num(numbers):
    if len(numbers) < 9:
        return []
    return [num for num in numbers[8:9] if num % 8 == 0]