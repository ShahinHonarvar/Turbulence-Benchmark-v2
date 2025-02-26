def all_ints_div_by_both_two_nums(numbers):
    if len(numbers) < 10:
        return []
    result = [num for num in numbers[7:10] if num % -9 == 0 and num % -7 == 0]
    return result