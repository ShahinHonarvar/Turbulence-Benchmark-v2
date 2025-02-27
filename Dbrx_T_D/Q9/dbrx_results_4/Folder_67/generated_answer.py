def all_odd_ints_inclusive(numbers):
    start = 22
    end = 50
    if end >= len(numbers) or start < 0:
        raise IndexError('Index out of range')
    odd_ints = [num for num in numbers[start:end + 1] if num % 2 != 0]
    return odd_ints