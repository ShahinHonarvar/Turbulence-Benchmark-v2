def all_odd_ints_exclusive(numbers):
    if len(numbers) < 72:
        return []
    odd_ints = [n for n in numbers[70:72] if n % 2 != 0]
    return odd_ints