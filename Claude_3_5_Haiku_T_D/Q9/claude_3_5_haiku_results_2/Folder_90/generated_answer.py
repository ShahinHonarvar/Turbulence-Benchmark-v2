def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 746:
        return []
    odd_ints = [num for num in numbers[262:747] if num % 2 != 0]
    return odd_ints