def sum_odd_ints_inclusive(numbers):
    total = 0
    for num in numbers[1:2]:
        if num % 2 != 0:
            total += num
    return total