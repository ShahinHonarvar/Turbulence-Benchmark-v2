def composite_nums_between_indices(numbers):
    return set((number for number in numbers[25:60] if number > 1 and (not all((number % divisor for divisor in range(2, number))))))