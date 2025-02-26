def all_ints_div_by_num(numbers):
    if len(numbers) < 2:
        return []
    return [num for num in numbers[:2] if num % 2 == 0]