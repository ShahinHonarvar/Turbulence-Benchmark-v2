def all_even_ints_inclusive(numbers):
    if len(numbers) <= 11:
        return [num for num in numbers[:11] if num % 2 == 0]
    else:
        return [num for num in numbers[:11] if num % 2 == 0]