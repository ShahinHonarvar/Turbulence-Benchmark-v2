def composite_nums_between_indices(numbers):
    composite_numbers = set((number for number in numbers[82:87] if number > 1 and (not all((number % divisor for divisor in range(2, number))))))
    return composite_numbers