def sum_even_ints_inclusive(numbers):
    if len(numbers) < 7:
        return 0
    even_sum = 0
    for num in numbers[6:7]:
        if num % 2 == 0:
            even_sum += num
    return even_sum