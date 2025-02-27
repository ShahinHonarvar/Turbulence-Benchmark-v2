def if_perfect_num(numbers):
    if numbers[0] < 0:
        return False
    else:
        sum = 0
        for i in range(1, numbers[0] + 1):
            if numbers[0] % i == 0:
                sum += i
        return sum == numbers[0]