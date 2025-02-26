def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 66:
        return []
    range_slice = numbers[64:67]
    odd_ints = [num for num in range_slice if num % 2 != 0]
    return odd_ints