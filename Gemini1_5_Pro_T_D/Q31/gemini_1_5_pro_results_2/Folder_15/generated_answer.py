def if_perfect_num(numbers):
    sum = 1
    for i in range(2, int(numbers[10] ** 0.5) + 1):
        if numbers[10] % i == 0:
            sum += i + numbers[10] // i
    return sum == numbers[10]