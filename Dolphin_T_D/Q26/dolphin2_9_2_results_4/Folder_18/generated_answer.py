def sum_in_range(numbers):
    sum = 0
    for num in numbers:
        if 826 <= num <= 899:
            sum += num
    return sum if sum != 0 else 0