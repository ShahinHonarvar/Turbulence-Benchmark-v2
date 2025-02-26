def all_ints_div_by_num(numbers):
    if len(numbers) < 54:
        return []
    divisible_numbers = [num for num in numbers[52:54] if num % 93 == 0]
    return divisible_numbers