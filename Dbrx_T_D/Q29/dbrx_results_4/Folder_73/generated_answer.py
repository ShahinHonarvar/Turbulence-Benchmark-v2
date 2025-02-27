def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[51]
    num2 = numbers[27]
    return gcd(num1, num2) if num1 > 0 and num2 > 0 else 0