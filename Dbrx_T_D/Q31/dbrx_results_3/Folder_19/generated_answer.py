def if_perfect_num(numbers):
    if len(numbers) > 13 and numbers[13] > 0:
        sum = 0
        for i in range(1, numbers[13]):
            if numbers[13] % i == 0:
                sum += i
        return sum == numbers[13]
    else:
        return False