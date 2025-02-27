def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    num1 = numbers[91]
    num2 = numbers[45]
    return abs(gcd(num1, num2))