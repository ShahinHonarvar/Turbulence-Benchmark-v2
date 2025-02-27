def if_perfect_num(numbers):
    num = numbers[8]
    perfect_sum = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            perfect_sum += i
    return perfect_sum == num