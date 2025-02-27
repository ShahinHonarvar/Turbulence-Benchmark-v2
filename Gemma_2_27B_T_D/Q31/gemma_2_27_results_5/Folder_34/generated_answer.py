def if_perfect_num(numbers):
    total = 1
    for i in range(2, int(numbers[97] ** 0.5) + 1):
        if numbers[97] % i == 0:
            total += i + numbers[97] // i
    return total == numbers[97]