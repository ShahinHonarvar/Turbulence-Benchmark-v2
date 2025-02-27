def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    number1 = numbers[46]
    number2 = numbers[13]
    return gcd(number1, number2)