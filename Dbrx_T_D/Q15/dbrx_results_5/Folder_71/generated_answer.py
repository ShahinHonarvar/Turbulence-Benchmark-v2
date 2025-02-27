def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 53:
        return 'Input list should have at least 53 elements.'
    odd_ints = [num for num in numbers[25:53] if num % 2 != 0]
    return sum(odd_ints) if odd_ints else 0