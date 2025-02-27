def sum_odd_ints_inclusive(numbers):
    if 1 < len(numbers) and numbers[1] % 2 != 0:
        return numbers[1]
    return 0