def all_ints_div_by_both_two_nums(numbers):
    if len(numbers) < 14:
        return []
    return [num for num in numbers[7:14] if num % 5 == 0 and num % 7 == 0]