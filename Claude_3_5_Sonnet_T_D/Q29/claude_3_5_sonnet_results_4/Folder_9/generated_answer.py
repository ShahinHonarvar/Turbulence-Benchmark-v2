def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 84 and len(numbers) > 63:
        num1 = numbers[84]
        num2 = numbers[63]
        return gcd(num1, num2)
    else:
        return None