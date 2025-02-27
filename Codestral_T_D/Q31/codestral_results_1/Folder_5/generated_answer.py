def if_perfect_num(numbers):
    index = 67
    num = numbers[index]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num