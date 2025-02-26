def all_even_ints_inclusive(numbers):
    if len(numbers) <= 746:
        return []
    result = [num for num in numbers[262:747] if num % 2 == 0]
    return result