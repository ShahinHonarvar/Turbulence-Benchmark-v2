def if_perfect_num(numbers):
    if numbers[63] > 0:
        sum = 0
        for i in range(1, numbers[63]):
            if numbers[63] % i == 0:
                sum += i
        if sum == numbers[63]:
            return True
    return False