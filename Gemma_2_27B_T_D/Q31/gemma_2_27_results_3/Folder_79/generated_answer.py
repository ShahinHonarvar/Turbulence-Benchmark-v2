def if_perfect_num(numbers):
    sum = 1
    for i in range(2, int(numbers[63] ** 0.5) + 1):
        if numbers[63] % i == 0:
            sum += i + numbers[63] // i
    return sum == numbers[63]