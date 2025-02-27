def if_perfect_number(numbers):
    num = numbers[132]
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum += i
    return sum == num