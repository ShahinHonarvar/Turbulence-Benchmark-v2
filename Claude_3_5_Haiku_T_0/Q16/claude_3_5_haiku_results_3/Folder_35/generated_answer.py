def sum_even_ints_inclusive(numbers):
    even_sum = 0
    for num in numbers[30:49]:
        if num % 2 == 0:
            even_sum += num
    return even_sum