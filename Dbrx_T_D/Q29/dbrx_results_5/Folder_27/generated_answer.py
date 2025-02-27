def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[15]
    num2 = numbers[40]
    common_factor = gcd(num1, num2)
    return common_factor