def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[66]
    num2 = numbers[56]
    num3 = numbers[92]
    return gcd(num1, gcd(num2, num3))