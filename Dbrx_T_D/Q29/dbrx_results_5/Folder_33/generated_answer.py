def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    number1 = numbers[166]
    number2 = numbers[106]
    return gcd(number1, number2) if number1 > 0 and number2 > 0 else 0