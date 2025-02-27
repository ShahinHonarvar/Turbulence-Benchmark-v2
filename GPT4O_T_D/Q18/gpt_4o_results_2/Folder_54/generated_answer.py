def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 92:
        return 0
    return sum((num for num in numbers[13:92] if num % -65 == 0 or num % -62 == 0))