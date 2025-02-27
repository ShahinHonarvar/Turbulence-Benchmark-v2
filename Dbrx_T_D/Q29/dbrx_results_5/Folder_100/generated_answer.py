def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[96]
    num2 = numbers[32]
    if num1 < 0 or num2 < 0:
        raise ValueError('All numbers must be positive')
    return gcd(num1, num2)