def all_even_ints_inclusive(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            numbers[i] = None
    numbers = [num for num in numbers if num is not None]
    return numbers[0:1] if len(numbers) > 0 else []