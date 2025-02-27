def if_perfect_num(numbers):
    num = numbers[132]
    sum = 1
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            sum += i
    return sum == num