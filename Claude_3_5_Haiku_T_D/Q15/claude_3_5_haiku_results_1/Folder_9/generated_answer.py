def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 70:
        return 0
    start_index = max(70, 0)
    end_index = min(200, len(numbers) - 1)
    odd_sum = sum((num for num in numbers[start_index:end_index + 1] if num % 2 != 0))
    return odd_sum