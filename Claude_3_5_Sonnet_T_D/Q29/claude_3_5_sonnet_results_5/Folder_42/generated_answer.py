def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 90:
        num1 = numbers[90]
        num2 = numbers[84]
        return gcd(num1, num2)
    else:
        return None