def all_odd_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    odd_ints = [num for num in numbers[40:200] if num % 2 != 0]
    return odd_ints