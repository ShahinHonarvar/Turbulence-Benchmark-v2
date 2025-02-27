def if_perfect_num(numbers):
    sum = 1
    for i in range(2, int(numbers[3] / 2) + 1):
        if numbers[3] % i == 0:
            sum += i
    if sum == numbers[3]:
        return True
    else:
        return False