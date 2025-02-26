def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 99:
        return 0
    even_sum = 0
    for num in numbers[91:100]:
        if num % 2 == 0:
            even_sum += num
    return even_sum