def if_perfect_num(numbers):
    sum = 1
    for i in range(2, int(numbers[2] ** 0.5) + 1):
        if numbers[2] % i == 0:
            sum += i + numbers[2] // i
    if sum == numbers[2] and numbers[2] != 1:
        return True
    else:
        return False