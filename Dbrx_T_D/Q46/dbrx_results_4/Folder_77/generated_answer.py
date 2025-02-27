def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers[693], numbers[331], numbers[668])
    gcf1, gcf2 = (gcd(num1, num2), gcd(num2, num3))
    return gcd(gcf1, gcf2) if gcf1 == gcf2 else gcd(gcf1, num1)