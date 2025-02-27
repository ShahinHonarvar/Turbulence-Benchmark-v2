def gcf_two_nums(numbers):
    num1, num2 = (numbers[95], numbers[85])

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    return gcd(lcm(num1, num2), min(num1, num2))