def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 975:
        return []
    odd_numbers = [num for num in numbers[639:976] if num % 2 != 0]
    return odd_numbers