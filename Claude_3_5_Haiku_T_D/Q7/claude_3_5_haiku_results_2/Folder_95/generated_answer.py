def all_even_ints_inclusive(numbers):
    if len(numbers) < 87:
        return []
    subset = numbers[82:87]
    return [num for num in subset if num % 2 == 0]