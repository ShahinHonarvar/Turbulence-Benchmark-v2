def gcf_two_nums(numbers):
    num1 = numbers[49]
    num2 = numbers[31]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(num1, num2)
    return gcf