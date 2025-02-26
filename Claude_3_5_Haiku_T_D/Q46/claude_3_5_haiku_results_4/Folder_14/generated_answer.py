def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[17]
    num2 = numbers[88]
    num3 = numbers[35]
    result = gcd(num1, gcd(num2, num3))
    return result