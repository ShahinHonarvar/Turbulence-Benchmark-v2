def if_perfect_num(numbers):
    total = 1
    for i in range(2, int(numbers[162] ** 0.5) + 1):
        if numbers[162] % i == 0:
            total += i + numbers[162] // i
    return total == numbers[162]