def if_perfect_num(numbers):
    total = 1
    for i in range(2, int(numbers[685] ** 0.5) + 1):
        if numbers[685] % i == 0:
            total += i + numbers[685] // i
    return total == numbers[685]