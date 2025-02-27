def if_perfect_num(numbers):
    if len(numbers) < 2:
        return False
    sum = 0
    for i in range(1, numbers[1] // 2 + 1):
        if numbers[1] % i == 0:
            sum += i
    return sum == numbers[1]