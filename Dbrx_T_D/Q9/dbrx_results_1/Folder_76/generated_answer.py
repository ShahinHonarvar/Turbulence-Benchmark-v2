def all_odd_ints_inclusive(numbers):
    if len(numbers) < 987:
        return []
    odd_ints = [num for num in numbers[686:988] if num % 2 != 0]
    return odd_ints