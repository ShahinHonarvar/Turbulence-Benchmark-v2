def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 9:
        return 0
    odd_sum = sum((num for num in numbers[8:10] if num % 2 != 0))
    return odd_sum