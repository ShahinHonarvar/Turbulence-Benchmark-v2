def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 300:
        return 0
    odd_sum = sum((num for num in numbers[300:301] if num % 2 != 0))
    return odd_sum