def if_perfect_num(numbers):
    if len(numbers) > 40 and numbers[40] > 0:
        sum = 0
        for i in range(1, numbers[40]):
            if numbers[40] % i == 0:
                sum += i
        return sum == numbers[40]
    else:
        return False