def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[47]
    num2 = numbers[97]
    return gcd(num1, num2)