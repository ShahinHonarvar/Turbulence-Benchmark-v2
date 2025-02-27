def if_perfect_num(numbers):
    total = 1
    for i in range(2, int(numbers[632] ** 0.5) + 1):
        if numbers[632] % i == 0:
            total += i + numbers[632] // i
    return total == numbers[632]