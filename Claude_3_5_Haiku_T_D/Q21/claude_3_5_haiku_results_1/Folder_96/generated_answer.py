def all_ints_div_by_num(numbers):
    if len(numbers) < 21:
        return []
    return [num for num in numbers[20:21] if num % 2 == 0]