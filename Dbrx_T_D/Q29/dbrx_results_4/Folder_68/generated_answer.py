def gcf_two_nums(numbers):

    def gcd(num1, num2):
        while num2 != 0:
            num1, num2 = (num2, num1 % num2)
        return num1
    num1 = numbers[8]
    num2 = numbers[9]
    return gcd(num1, num2)