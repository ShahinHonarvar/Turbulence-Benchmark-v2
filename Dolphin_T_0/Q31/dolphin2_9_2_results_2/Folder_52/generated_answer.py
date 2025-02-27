def if_perfect_num(numbers):
    num = numbers[478]
    factors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            factors_sum += i
    if factors_sum == num:
        return True
    else:
        return False