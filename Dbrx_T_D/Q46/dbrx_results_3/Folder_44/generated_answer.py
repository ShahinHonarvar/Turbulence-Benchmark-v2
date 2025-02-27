def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[62]
    num2 = numbers[96]
    num3 = numbers[26]
    gcf = gcd(num1, gcd(num2, num3))
    return gcf