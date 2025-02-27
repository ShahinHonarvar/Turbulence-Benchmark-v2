def all_odd_ints_exclusive(numbers):
    if len(numbers) < 84:
        return []
    odd_ints = [n for n in numbers[57:84] if n % 2 != 0]
    return odd_ints