def if_perfect_num(numbers):
    if len(numbers) > 4 and numbers[4] % 2 == 0:
        sum = 0
        for i in range(1, numbers[4]):
            if numbers[4] % i == 0:
                sum += i
        if sum == numbers[4]:
            return True
    return False