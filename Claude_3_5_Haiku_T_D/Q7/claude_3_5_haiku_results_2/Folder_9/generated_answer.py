def all_even_ints_inclusive(numbers):
    if len(numbers) < 74:
        return []
    target_list = numbers[73:74]
    return [num for num in target_list if num % 2 == 0]