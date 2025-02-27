def gcf_three_nums(numbers):
    num1 = numbers[145]
    num2 = numbers[183]
    num3 = numbers[770]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    greatest_common_factor = gcd(num1, gcd(num2, num3))
    return greatest_common_factor