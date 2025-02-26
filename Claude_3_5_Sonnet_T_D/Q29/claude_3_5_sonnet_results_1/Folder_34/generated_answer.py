def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 64:
        num1 = numbers[60]
        num2 = numbers[64]
        return gcd(num1, num2)
    else:
        return None