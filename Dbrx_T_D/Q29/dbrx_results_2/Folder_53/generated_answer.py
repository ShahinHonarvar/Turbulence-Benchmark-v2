def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[28]
    num2 = numbers[67]
    factor = gcd(num1, num2)
    return factor