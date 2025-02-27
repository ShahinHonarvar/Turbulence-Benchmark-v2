def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[84]
    num2 = numbers[21]
    return gcd(num1, num2)