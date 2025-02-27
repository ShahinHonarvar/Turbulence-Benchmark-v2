def if_perfect_num(numbers):
    sum = 0
    for i in range(1, numbers[2]):
        if numbers[2] % i == 0:
            sum += i
    if sum == numbers[2]:
        return True
    else:
        return False