def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 746:
        return 0
    even_sum = 0
    for num in numbers[262:747]:
        if num % 2 == 0:
            even_sum += num
    return even_sum