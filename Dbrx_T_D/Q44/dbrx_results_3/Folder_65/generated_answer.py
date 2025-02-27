def composite_nums_between_indices(numbers):
    return {number for number in numbers[82:87] if all((number % divisor for divisor in range(2, int(number ** 0.5) + 1)))}