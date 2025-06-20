def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[32]
    num2 = numbers[54]
    num3 = numbers[13]
    result = gcd(gcd(num1, num2), num3)
    return result