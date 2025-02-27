def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 87:
        return 0
    return sum((num for num in numbers[68:87] if num % 2 != 0))