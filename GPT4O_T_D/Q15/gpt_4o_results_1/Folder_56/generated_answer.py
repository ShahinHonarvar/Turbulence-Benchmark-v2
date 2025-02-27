def sum_odd_ints_inclusive(numbers):
    if not numbers:
        return 0
    total = 0
    for num in numbers[0:1]:
        if num % 2 != 0:
            total += num
    return total