def if_perfect_num(numbers):
    if len(numbers) > 247 and numbers[247] > 0:
        sum = 0
        for i in range(1, numbers[247]):
            if numbers[247] % i == 0:
                sum += i
        return sum == numbers[247]
    else:
        return False