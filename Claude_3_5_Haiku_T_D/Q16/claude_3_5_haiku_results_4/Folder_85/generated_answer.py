def sum_even_ints_inclusive(numbers):
    if len(numbers) < 9:
        return 0
    slice_range = numbers[6:9]
    even_ints = [num for num in slice_range if num % 2 == 0]
    return sum(even_ints) if even_ints else 0