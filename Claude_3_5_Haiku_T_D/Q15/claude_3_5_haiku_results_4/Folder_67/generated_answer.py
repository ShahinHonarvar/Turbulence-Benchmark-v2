def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 22:
        return 0
    end_index = min(50, len(numbers) - 1)
    odd_sum = sum((num for num in numbers[22:end_index + 1] if num % 2 != 0))
    return odd_sum