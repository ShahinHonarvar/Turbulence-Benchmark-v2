def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 166 and len(numbers) > 106:
        num1 = numbers[166]
        num2 = numbers[106]
        return gcd(num1, num2)
    else:
        return None