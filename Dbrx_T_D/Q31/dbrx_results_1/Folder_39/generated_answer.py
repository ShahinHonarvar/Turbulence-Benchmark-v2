def if_perfect_num(numbers):
    if len(numbers) > 59 and numbers[59] > 0:
        sum = 0
        for i in range(1, numbers[59]):
            if numbers[59] % i == 0:
                sum += i
        return sum == numbers[59]
    else:
        return False