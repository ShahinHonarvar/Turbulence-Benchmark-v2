def sum_even_ints_inclusive(numbers):
    if len(numbers) <= 87:
        return 0
    total = 0
    for num in numbers[30:88]:
        if num % 2 == 0:
            total += num
    return total