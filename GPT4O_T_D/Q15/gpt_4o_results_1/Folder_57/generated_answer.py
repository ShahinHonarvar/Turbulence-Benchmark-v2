def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 28:
        return 0
    sublist = numbers[27:56]
    return sum((x for x in sublist if x % 2 != 0))