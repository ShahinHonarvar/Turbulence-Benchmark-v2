def if_perfect_num(numbers):
    num = numbers[92]
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum = sum + i
    return sum == num