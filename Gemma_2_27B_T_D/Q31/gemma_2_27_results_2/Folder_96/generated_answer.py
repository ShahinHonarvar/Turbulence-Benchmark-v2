def if_perfect_num(numbers):
    sum = 1
    for i in range(2, int(numbers[47] ** 0.5) + 1):
        if numbers[47] % i == 0:
            sum += i + numbers[47] / i
    return sum == numbers[47]