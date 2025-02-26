def all_ints_div_by_both_two_nums(numbers):
    if len(numbers) < 10:
        return []
    return [num for num in numbers[6:10] if num % -1 == 0 and num % -10 == 0]