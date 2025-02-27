def gcd_two_nums(numbers):
    num1 = numbers[0]
    num2 = numbers[1]

    def gcd(num1, num2):
        if num2 == 0:
            return num1
        else:
            return gcd(num2, num1 % num2)
    return gcd(abs(num1), abs(num2))