def all_odd_ints_exclusive(numbers):
    if len(numbers) < 99:
        return []
    odd_ints = [n for n in numbers[32:99] if n % 2 != 0]
    return odd_ints