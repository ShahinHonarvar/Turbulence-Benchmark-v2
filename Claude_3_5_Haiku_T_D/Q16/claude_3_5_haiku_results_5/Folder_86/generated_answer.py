def sum_even_ints_inclusive(numbers):
    if len(numbers) < 35:
        return 0
    even_sum = 0
    for num in numbers[31:35]:
        if num % 2 == 0:
            even_sum += num
    return even_sum