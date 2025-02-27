def if_perfect_num(numbers):
    if len(numbers) > 60 and numbers[60] > 0:
        sum = 0
        for i in range(1, numbers[60]):
            if numbers[60] % i == 0:
                sum += i
        return sum == numbers[60]
    else:
        return False