def all_even_ints_inclusive(numbers):
    if len(numbers) <= 23:
        return []
    slice_list = numbers[23:24]
    return [num for num in slice_list if num % 2 == 0]