def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 88 and len(numbers) > 35:
        num1 = numbers[88]
        num2 = numbers[35]
        return gcd(num1, num2)
    else:
        return None