def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2 = (numbers[86], numbers[89])
    return gcd(num1, num2) if num1 > 0 else 0