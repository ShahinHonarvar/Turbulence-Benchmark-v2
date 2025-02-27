def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers[21], numbers[51], numbers[33])
    gcf1 = gcd(numbers[21], numbers[51])
    result = gcd(gcf1, numbers[33])
    return result