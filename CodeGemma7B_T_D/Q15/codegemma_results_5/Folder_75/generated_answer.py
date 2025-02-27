def sum_odd_ints_inclusive(numbers):
    sum = 0
    for x in numbers[56:58]:
        if x % 2 != 0:
            sum += x
    return sum