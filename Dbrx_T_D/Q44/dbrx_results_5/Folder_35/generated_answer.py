def composite_nums_between_indices(numbers):
    composite_numbers = set((num for num in numbers[28:33] if num > 1 and num % 2 == 0 or num % 3 == 0))
    return composite_numbers