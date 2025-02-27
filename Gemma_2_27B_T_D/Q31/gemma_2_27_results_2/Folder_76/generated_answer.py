def if_perfect_num(numbers):
    total = 1
    for i in range(2, int(numbers[537] ** 0.5) + 1):
        if numbers[537] % i == 0:
            total += i + numbers[537] // i
    return total == numbers[537]