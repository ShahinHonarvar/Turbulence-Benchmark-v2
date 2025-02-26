def all_ints_not_div_by_num(numbers):
    if len(numbers) <= 15:
        return []
    return [num for num in numbers[15:21] if num % -93 != 0]