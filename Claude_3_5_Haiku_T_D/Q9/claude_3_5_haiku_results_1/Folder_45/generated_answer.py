def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 200:
        return []
    odd_integers = [num for num in numbers[30:201] if num % 2 != 0]
    return odd_integers