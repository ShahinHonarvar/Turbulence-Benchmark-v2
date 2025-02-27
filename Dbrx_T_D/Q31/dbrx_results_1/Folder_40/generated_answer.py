def if_perfect_num(numbers):
    if len(numbers) > 7 and numbers[7] % 1 == 0 and (numbers[7] > 0):
        sum = 0
        for i in range(1, numbers[7]):
            if numbers[7] % i == 0:
                sum += i
        if sum == numbers[7]:
            return True
    return False