def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 71:
        return 0
    even_sum = 0
    for num in numbers[52:72]:
        if num % 2 == 0:
            even_sum += num
    return even_sum