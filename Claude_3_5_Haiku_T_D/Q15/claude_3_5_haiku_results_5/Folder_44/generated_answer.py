def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 68:
        return 0
    odd_sum = sum((num for num in numbers[13:69] if num % 2 != 0))
    return odd_sum