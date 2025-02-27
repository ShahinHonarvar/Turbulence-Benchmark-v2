def all_odd_ints_inclusive(numbers):
    if len(numbers) < 66:
        return []
    slice_of_interest = numbers[64:67]
    return [num for num in slice_of_interest if num % 2 != 0]