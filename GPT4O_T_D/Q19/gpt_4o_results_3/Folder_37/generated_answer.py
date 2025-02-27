def all_ints_not_div_by_num(numbers):
    return [num for num in numbers[2:len(numbers) - 1] if num % 5 != 0]