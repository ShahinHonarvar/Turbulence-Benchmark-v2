def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    num1 = numbers[56]
    num2 = numbers[92]
    return gcd(num1, num2)