def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 23:
        return 'List is too short.'
    elif 23 > len(numbers) - 23:
        return 'List is too short.'
    else:
        return sum((num for num in numbers[23:] if num % 2 != 0 and num % 2 != -1))