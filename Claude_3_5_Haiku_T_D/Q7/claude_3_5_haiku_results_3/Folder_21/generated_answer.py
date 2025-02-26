def all_even_ints_inclusive(numbers):
    if len(numbers) <= 975:
        return []
    slice_range = numbers[639:976]
    return [num for num in slice_range if num % 2 == 0]