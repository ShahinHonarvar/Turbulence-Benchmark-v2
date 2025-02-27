def gcd_two_nums(numbers):
    num1 = numbers[360]
    num2 = numbers[722]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return abs(num1)