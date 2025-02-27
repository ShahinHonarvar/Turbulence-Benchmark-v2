def composite_nums_between_indices(numbers):
    return {num for num in numbers[22:89] if not (num < 2 or (num % 2 == 0 and num > 2) or (num % 3 == 0 and num > 3))}