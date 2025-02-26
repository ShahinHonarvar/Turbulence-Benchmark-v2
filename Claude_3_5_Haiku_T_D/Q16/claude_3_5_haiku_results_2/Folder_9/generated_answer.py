def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 200:
        return 0
    total = 0
    for num in numbers[70:201]:
        if num % 2 == 0:
            total += num
    return total