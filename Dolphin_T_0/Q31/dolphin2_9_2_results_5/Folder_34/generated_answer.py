def if_perfect_num(numbers):
    num = numbers[97]
    s = 1
    for i in range(2, num):
        if num % i == 0:
            s += i
    return s == num