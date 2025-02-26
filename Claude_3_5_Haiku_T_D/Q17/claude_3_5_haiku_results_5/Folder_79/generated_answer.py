def all_ints_div_by_both_two_nums(numbers):
    if len(numbers) < 10:
        return []
    return [num for num in numbers[8:10] if num % -3 == 0 and num % 6 == 0]