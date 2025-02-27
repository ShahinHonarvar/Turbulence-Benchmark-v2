def gcf_three_nums(numbers):
    num1, num2, num3 = (numbers[90], numbers[54], numbers[96])

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    return gcd(gcd(num1, num2), num3)