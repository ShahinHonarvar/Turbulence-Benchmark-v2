def if_perfect_num(numbers):
    if len(numbers) > 100:
        sum = 1
        for i in range(2, int(numbers[100] ** 0.5) + 1):
            if numbers[100] % i == 0:
                sum += i + numbers[100] / i
        return sum == numbers[100]
    return False