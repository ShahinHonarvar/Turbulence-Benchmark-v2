def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[86]
    num2 = numbers[89]
    return gcd(num1, num2)