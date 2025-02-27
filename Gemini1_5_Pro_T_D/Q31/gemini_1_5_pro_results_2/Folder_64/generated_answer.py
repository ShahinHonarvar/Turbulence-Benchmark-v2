def if_perfect_num(numbers):
    sum = 1
    for i in range(2, int(numbers[1] / 2) + 1):
        if numbers[1] % i == 0:
            sum += i
    if sum == numbers[1]:
        return True
    else:
        return False