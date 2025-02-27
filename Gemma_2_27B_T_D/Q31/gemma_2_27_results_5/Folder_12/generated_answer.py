def if_perfect_num(numbers):
    total = 1
    for i in range(2, int(numbers[27] ** 0.5) + 1):
        if numbers[27] % i == 0:
            total += i + numbers[27] // i
    return total == numbers[27]