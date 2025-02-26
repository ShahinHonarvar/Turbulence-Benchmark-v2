def all_even_ints_exclusive(numbers):
    if len(numbers) <= 102:
        return []
    sublist = numbers[101:-1]
    return [num for num in sublist if num % 2 == 0]