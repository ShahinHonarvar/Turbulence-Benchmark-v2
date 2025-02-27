def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[38]
    num2 = numbers[77]
    return gcd(num1, num2)