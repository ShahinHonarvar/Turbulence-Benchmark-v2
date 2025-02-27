def all_ints_not_div_by_num(numbers):
    if len(numbers) <= 64:
        return []
    return [num for num in numbers[64:73] if num % -99 != 0]