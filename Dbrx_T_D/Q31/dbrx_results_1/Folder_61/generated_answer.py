def if_perfect_num(numbers):
    if len(numbers) > 8 and numbers[8] % 2 == 0:
        sum = 0
        for i in range(1, numbers[8]):
            if numbers[8] % i == 0:
                sum += i
        if sum == numbers[8]:
            return True
    return False