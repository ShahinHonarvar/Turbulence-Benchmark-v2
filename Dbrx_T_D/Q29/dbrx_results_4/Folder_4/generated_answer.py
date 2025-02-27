def gcf_two_nums(numbers):
    num1 = numbers[76]
    num2 = numbers[57]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    return lambda: lcm(num1, num2)() if num1 > 0 and num2 > 0 else 0