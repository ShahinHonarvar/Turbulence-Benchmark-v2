def if_perfect_num(numbers):
    num = numbers[1]
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum = sum + i
    if sum == num:
        return True
    else:
        return False