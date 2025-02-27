def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[48]
    num2 = numbers[74]
    return gcd(num1, num2) if num1 > 0 and num2 > 0 else None