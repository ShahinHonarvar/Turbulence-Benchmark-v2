def if_perfect_num(numbers):
    total = 1
    for i in range(2, int(numbers[15] ** 0.5) + 1):
        if numbers[15] % i == 0:
            total += i + numbers[15] // i
    return total == numbers[15]