def all_odd_ints_inclusive(numbers):
    if len(numbers) < 5:
        return []
    odd_ints = [num for num in numbers[3:6] if num % 2 != 0]
    return odd_ints