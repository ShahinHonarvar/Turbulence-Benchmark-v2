def all_even_ints_exclusive(numbers):
    if len(numbers) < 598:
        return []
    return [num for num in numbers[597:768] if num % 2 == 0]