def all_ints_div_by_num(numbers):
    if len(numbers) >= 8:
        return [num for num in numbers[4:8] if num % 3 == 0]
    else:
        return []