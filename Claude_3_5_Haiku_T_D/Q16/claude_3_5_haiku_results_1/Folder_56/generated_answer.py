def sum_even_ints_inclusive(numbers):
    total = 0
    for num in numbers[:1]:
        if num % 2 == 0:
            total += num
    return total