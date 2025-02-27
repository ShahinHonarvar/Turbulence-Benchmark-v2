def if_perfect_num(numbers):
    index = 132
    num = numbers[index]
    perfect_sum = 0
    for i in range(1, num):
        if num % i == 0:
            perfect_sum += i
    return perfect_sum == num