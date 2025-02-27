def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[341]
    num2 = numbers[238]
    num3 = numbers[374]
    return gcd(gcd(num1, num2), num3)