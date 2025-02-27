def all_ints_inclusive(numbers):
    if len(numbers) < 402:
        return 'Input list should have at least 402 elements'
    else:
        return numbers[200:201] + numbers[200:402][::-1]