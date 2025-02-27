def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    num1 = numbers[64]
    num2 = numbers[80]
    num3 = numbers[15]
    return lcm(gcd(num1, num2), num3)