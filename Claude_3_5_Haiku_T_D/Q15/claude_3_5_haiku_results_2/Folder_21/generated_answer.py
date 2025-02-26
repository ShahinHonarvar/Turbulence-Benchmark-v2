def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 975:
        return 0
    total = 0
    for i in range(639, 976):
        if numbers[i] % 2 != 0:
            total += numbers[i]
    return total