def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 49:
        return 0
    even_sum = 0
    for num in numbers[35:50]:
        if num % 2 == 0:
            even_sum += num
    return even_sum