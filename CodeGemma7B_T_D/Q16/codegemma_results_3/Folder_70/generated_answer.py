def sum_even_ints_inclusive(numbers):
    sum = 0
    for n in numbers[28:33]:
        if n % 2 == 0:
            sum += n
    return sum if sum else 0