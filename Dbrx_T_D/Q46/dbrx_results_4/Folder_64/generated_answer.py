def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    num1 = numbers[0]
    num3 = numbers[3]
    num8 = numbers[8]
    gcf = gcd(num1, gcd(num3, num8))
    return gcf