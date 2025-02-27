def all_odd_ints_inclusive(numbers):
    if len(numbers) < 750:
        return []
    odd_ints = [num for num in numbers[246:751] if num % 2 != 0]
    return odd_ints