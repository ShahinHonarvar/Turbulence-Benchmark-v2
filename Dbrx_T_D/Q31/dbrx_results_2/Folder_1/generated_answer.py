def if_perfect_num(numbers):
    if len(numbers) > 85 and numbers[85] > 0:
        sum = 0
        for i in range(1, numbers[85]):
            if numbers[85] % i == 0:
                sum += i
        return sum == numbers[85]
    else:
        return False